# The __init__ manages imports, creates necessary objects, and configuration of the application.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.sqlite3"
db = SQLAlchemy(app)
