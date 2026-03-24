from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from dotenv import load_dotenv
import os

FILE_DL_PATH = os.getenv("FILE_DL_PATH")
# load environment variables
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# SETUP LOGIN LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
# Define User model with UserMixin. Thanks to UserMixin our user have 3 extra features😀: is_active,
# is_authenticated, is_anonymous


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        check_mail = db.session.execute(
            db.select(User).where(User.email == request.form.get("email"))
        ).scalar()
        if check_mail:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        else:
            hashed_password = generate_password_hash(
                request.form.get("password"), method="pbkdf2:sha256", salt_length=8
            )
            new_user = User(
                email=request.form.get("email"),
                password=hashed_password,
                name=request.form.get("name"),
            )
            db.session.add(new_user)
            db.session.commit()

            # Login and authenticate user after adding details to database
            login_user(new_user)

            return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user in db
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        # check stored password hash against entred passsword hash
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Password incorrect, please try again.")
                return redirect(url_for("login"))
        else:
            flash("That email does not exist, please try again!")
            return redirect(url_for("login"))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", logged_in=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", path=f"{FILE_DL_PATH}", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
