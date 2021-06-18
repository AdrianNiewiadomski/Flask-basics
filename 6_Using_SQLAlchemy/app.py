from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

# We have to add a config to our app.
# Notice the word books.sqlite3 in the URI. This is the name of the in-file database we are referencing.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.sqlite3"
# The URI points to the place where a database is located. It is currently in the same directory as the script.

db = SQLAlchemy(app)


class Book(db.Model):
    id = Column("id", Integer, primary_key=True)
    author = Column("author", String(20), nullable=False)
    # If we do not define name of the column the variable name will be taken.
    title = Column(String(100), nullable=False)
    published_date = Column(Integer)

    def __init__(self, author, title, published_date):
        self.author = author
        self.title = title
        self.published_date = published_date

    def __str__(self):
        return f"Book({self.author}, {self.title}, {self.published_date})"


def insert_book(author, title, published_date):
    book = Book(author, title, published_date)
    db.session.add(book)
    db.session.commit()


def select_books_by_author(author):
    books = Book.query.filter_by(author=author).all()
    for book in books:
        print('book: ', book)
    return books


def select_all_books():
    books = Book.query.all()
    for book in books:
        print('book: ', book)
    return books


@app.route("/")
@app.route("/<author>")
def display_books(author=None):
    books = None
    if author:
        books = select_books_by_author(author)
    else:
        books = select_all_books()
    return render_template("index.html", books=books)


if __name__ == "__main__":
    # This will create a database if it does not exist.
    db.create_all()

    insert_book("Tolkien", "Hobbit", 2004)
    insert_book("Rowling", "Harry Potter", 1997)

    app.run()
