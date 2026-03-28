from enum import auto, unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# Create the database
class Base(DeclarativeBase):
    pass


# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Crate the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    # This will set the table name, default is python will use the class name in snake_case
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()


# Create record
with app.app_context():
    new_book = Books(
        id=1, title="Pride and Prejudice", author="Jane Austen", rating=9.3
    )

    db.session.add(new_book)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
