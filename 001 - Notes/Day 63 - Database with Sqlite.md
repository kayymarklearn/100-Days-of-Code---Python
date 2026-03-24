2026-03-20 15:40

Status: incomplete

Tags:


# **Databases**
>Databases allow us to store persistent data in our applications (eg. user data like passwords, emails and usernames.)
>The most used database in the world is SQLite. It's so popular that it's included by default in all Python installations, so if you're creating a Python project, you've already got it installed.
>Creating a database is as simple as importing the sqlite3 module/package
>```
>import sqlite3
>
db = sqlite3.connect('books-collection.db')
> # Next we need to create a **cursor** which will control our database
> cursor = db.cursor()
>```
>So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.
>
>CREATING TABLES IN THE DB
>Coming back to the Excel analogy, a single Excel file can contain many tables (sheets), each tab is a different table. To create a table we execute the sql query using our cursor.
>```
>`cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")`
>```
>## Check the [References](#References) for a guide to sql to understand the query.
>In order to view our database we need an application like db browser or any other specialized software like dbeaver or sqlite browser.
>To add data we can execute a query with cursor.
>```
>cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
	# This will create a query for Harry Porter and commit the changes to our database.
	# Note that SQL queries are very sensitive to typos.
>```
> Luckily, there are much better ways of working with SQLite in python projects, we can use a tool called SQLAlchemy to write python code instead of all these error prone SQL commands.

#### Code Example
> 	```
> 	import sqlite3
>
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()>
 # cursor.execute(
 >#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
v# )
v# cursor.execute("INSERT INTO books VALUES(1, 'Harry Porter', 'J. K. Rowling', '9.3')")
cursor.execute(
    "INSERT INTO books VALUES(2, 'Pride and Prejudice', 'Jane Austen', '9.6')"
)
db.commit()
> ```

### SQLAlchemy
> is defined as an ORM (Object Relational Mapping) library. 
>  SQLAlchemy is defined as an **ORM** (Object Relational Mapping) library. This means that it's able to map the relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object. This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy. An implementation of the above is SQLAlchemy is below
>  ```
>  from enum import auto, unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
>
app = Flask(__name__)
>
 # Create the database
>class Base(DeclarativeBase):
  >  pass
>
 # Configure the SQLite database, relative to the app instance folder
 >app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
>
 # Crate the extension
>db = SQLAlchemy(model_class=Base)
>
 # initialize the app with the extension
>db.init_app(app)
>
class Books(db.Model):
    # This will set the table name, default is python will use the class name in snake_case
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
>
    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f"<Book {self.title}>"
>
 # Create table schema in the database. Requires application context
>with app.app_context():
    db.create_all()
># Create record
with app.app_context():
    new_book = Books(
        id=1, title="Pride and Prejudice", author="Jane Austen", rating=9.3
    )
>
    db.session.add(new_book)
    db.session.commit()
>
if __name__ == "__main__":
    app.run(debug=True)
>  ```
>In addition to the initial setup, the most crucial thing to figure out when working with any database technology is how to CRUD data records.
>- **Create A New Record**
>```
>with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
>```
> #Note When creating records, the primary key field is optional as it will be automatically generated.
> `new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)`
>
>- **Read a record**
>To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a `Result` object). We then use `scalars()` to get the individual elements rather than entire rows.
>
  Read All Records
> ```
	with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
>```
> 
  Read A Particular Record By Query
> ```with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar() ```
  To get a single element we can use `scalar()` instead of `scalars()`.
>
>- **Update a record**
> Update A Particular Record By Query
>```with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() ```
>
 Update A Record By PRIMARY KEY
>```book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()```
>
>		
>- **Delete a record** 
>```book_id = 1
>with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit() ```
>
  You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the `get_or_404()` method is quite handy.
  #Note Adding .all() to a select query returns a list not just an SQLAlchemy Object
  #Note NOTE: HTML forms (WTForms included) [do not accept PUT, PATCH or DELETE methods](https://softwareengineering.stackexchange.com/questions/114156/why-are-there-are-no-put-and-delete-methods-on-html-forms). So while this would normally be a PUT request (replacing existing data), because the request is coming from a HTML form, you should accept the edited post as a POST request.

#Note In order to allow a file to be downloaded, we use a Flask method called send_from_directory()


## References
[Learn SQL](https://www.codecademy.com/article/sql-commands)
[Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/)
