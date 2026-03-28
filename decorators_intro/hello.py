from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1> \
#     <hr/> \
#     <p>This is a paragraph</p>'


# @app.route("/home")
# def home():
#     return "<a href='/'>Home dir!</a>"


# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name} you are {number} years old!"
def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"

    return bold


def make_emphasis(func):
    def emphasis():
        return f"<em>{func()}</em>"

    return emphasis


def make_underline(func):
    def underline():
        return f"<u>{func()}</u>"

    return underline


@app.route("/")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/<name>/<int:age>")
def greet(name, age):
    return f"Hello {name}, you are {age} years old!"


if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)
