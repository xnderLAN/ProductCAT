from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User
from . import login_manager
from .forms import LogForm

views = Blueprint("views", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first() 

@views.get("/")
def index():
    form = LogForm()
    check_user = User.objects(email="theghiles@gmail.com").first()
    print(check_user)

    return render_template("login.html", form=form)