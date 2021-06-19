from flask import render_template, request

from mvc_app import app, db
from mvc_app.model import Book

# We have to add a config to our mvc_app.
# Notice the word books.sqlite3 in the URI. This is the name of the in-file database we are referencing.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.sqlite3"


# The URI points to the place where a database is located. It is currently in the same directory as the script.


def insert_book(author, title, published_date):
    # To insert a record into the database you have to add a record and commit it.
    db.session.add(Book(author, title, published_date))
    db.session.commit()


def select_books_by_author(author):
    # The select query takes the following form with SQLAlchemy:
    return Book.query.filter_by(author=author).all()


def select_all_books():
    return Book.query.all()


@app.route("/books")
def display_books():
    # The data from the filtering form can be passed in request.args.
    if "author" in request.args.keys():
        return render_template("index.html", books=select_books_by_author(request.args.get("author")))
    else:
        return render_template("index.html", books=select_all_books())


if __name__ == "__main__":
    # This will create a database if it does not exist.
    db.create_all()

    # Add some books to the table if it is empty.
    if len(select_all_books()) == 0:
        insert_book("Tolkien", "Hobbit", 2004)
        insert_book("Rowling", "Harry Potter", 1997)
        insert_book("Martin", "A Game of Thrones", 1996)
        insert_book("Rothfuss", "The Name of the Wind", 2007)

    app.run()
