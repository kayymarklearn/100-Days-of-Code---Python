2026-03-06 10:06

Status: Incomplete
Tags: [[Day 55 - Advanced Decorators, HTML Rendering, Parsing URLs and Flask Debugging]]
[[Day 56 - Rendering HTML static files Using website Templates]]
[[Day 57 - Templating with Jinja in Flask apps]]
# **Understanding Backend Web Dev**
> In order to build a fully functional web site or app, we need the front end (where the user interacts with the service), these are made with technologies such as html, css and javascript, we also need the backend.
> The backend has three compoents: Client, Server and Database.
> - Client - basically the user accessing the browser, this is the part that faces the user.
> - Server - basically a powerful computer that's hooked up to the internet, always ready to receive and process requests.
> - Database - basically the data storage system that stores all information and data.
> ![[Client-server-db.jpg|684]]
> If we use a restaurant analogy, the client will be the area where customers order, the server would be the kitchen that takes and processes orders and the database will be the storage and cold rooms where groceries  and other cooking essentials are stored.

### Creating a web server with Flask
> To start a flask application we can use the boilerplate
> ```
> from flask import Flask
> app = Flask(__name__)
> @app.route('/')
> def hello_world():
> 	return "Hello world!"
> ```
> After creating the app
> set the env variable to the name of the file
> `export FLASK_APP=main.py`
> then spin it up with 
> `flask run`

#### `__name__` and `__main__` special attributes
> These are built in special attributes.
> - `__name__`: the name of class, function, method, descriptor or generator instance.
> - `__main__`: is the name of the scope in which top level code executes. A module's __name__ is set equal to `__main__` when read from standard input, script or interactive prompt.

#### First class objects and nested functions

> Python functions are treated as first calss objects, that means they can be passed around as arguments just like strings/ integers/floats etc.
>```
>def add(n1, n2):
    return n1 + n2
>
def subtract(n1, n2):
    return n1 - n2
>
def multiply(n1, n2):
    return n1 * n2
>
def divide(n1, n2):
    return n1 / n2
>
def calc(calc_func, n1, n2):
    return calc_func(n1, n2)
>
print (calc(multiply, 2, 4)) # prints 8
print(calc(subtract, 5, 1)) # prints 4
>
>```
>Functions can also be nested in other functions.
>```
># Nested functions [They can be nested inside other functions]
def outer_function():
    print("I'm outer")
    >
    def nested_function():
        print("I'm inner")
    # nested function will run when run inside the outer functions
    # nested_function()
>
    # Returning a nested function
    return nested_function
>
#outer_function()
#if we try to call the inner function outside the outside function, we get a out of scope error.
#nested_function()
>
#But.... functions can also be returned from other functions
inner_function = outer_function()
inner_function()
>
>```

#### Python decorators
> > A decorator function is a function that gives additional functionality to an  already existing function by essentially wrapping it or modifying it's functionality
> > the `@decorator` is what we call syntactic sugar, we could as well call the name of the function and pass in the name of our function.
> > ```
> > Python decorator functiony
import time
def decorator_function(function):
    def wrapper_function():
        function()
>
    return wrapper_function
>
in order to add the delay to all functions, we can add the decorator
def delay_decorator(function):
    def sec_2_delay():
        time.sleep(2)
        # Do something before
        function()
        #function() # you could even run it twice 😂
        print(function.__name__)
        # Do something after
    return sec_2_delay
>
Now to apply decorator to all the function definitions we want to delay we can add the @decorator 
>
def say_hello():
    print("Hello 👋")
>
@delay_decorator
def say_bye():
    print("Bye 👋")
>
@delay_decorator
def say_greeting():
    print("How are your? 🫂")
>
say_hello()
say_bye()
say_greeting()
>
>
> > ```


#### Advanced Decorators with Args and Kwargs
```
## Advance python decorators


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_auth(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            print(func.__name__)
            func(args[0])

    return wrapper


@is_auth
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Mark")
new_user.is_logged_in = True
create_blog_post(new_user)

```

## References
