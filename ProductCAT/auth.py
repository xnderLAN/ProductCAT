import email
from tabnanny import check
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import logout_user, login_user
from .forms import RegForm, LogForm
from werkzeug.security import generate_password_hash
from .models import *
auth = Blueprint("auth", __name__)

@auth.post("/login")
def login():
    form = LogForm()
    if form.validate_on_submit():
        check_user = User.objects(email=form.email.data).first()
        if check_user:
            pass


    return redirect(url_for("views.index"))

@auth.route("/register", methods=["POST", "GET"])
def register():
    logout_user()
    form = RegForm()
    if request.method == "POST":
        if form.validate_on_submit():
            password_hash = generate_password_hash(form.password.data)
            user = User(
                email=form.email.data,
                username=form.username.data,
                name=form.name.data,
                password_hash=password_hash,
            )
            user.save()
            flash("Thanks for registering!", category="success")
            return url_for("views.login")
    return render_template("register.html")