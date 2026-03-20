from flask import Flask, render_template, request

app = Flask("__name__")
user_name = ""
user_pass = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    user_name = request.form["username"]
    user_pass = request.form["password"]

    return f"<h1>Username is: {user_name}, Password is: {user_pass}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
