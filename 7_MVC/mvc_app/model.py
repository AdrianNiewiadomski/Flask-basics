# Add this import to calm down PyCharm Code Inspection ;)
from sqlalchemy import Column, Integer, String

from . import db


class Book(db.Model):
    # We define table columns with their names and data types. The table should have a primary key.
    id = Column("id", Integer, primary_key=True)
    # The author's name cannot be null.
    author = Column("author", String(20), nullable=False)
    # If we do not define the name of the column, the variable name will be taken.
    title = Column(String(100), nullable=False)
    published_date = Column(Integer)

    def __init__(self, author, title, published_date):
        self.author = author
        self.title = title
        self.published_date = published_date

    def __str__(self):
        return f"Book({self.author}, {self.title}, {self.published_date})"
