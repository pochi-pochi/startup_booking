from flask import request

from flask import Blueprint, render_template

from app.app import db
from app.user_crud.models import Users


user_crud = Blueprint(
    "user_crud",
    __name__,
    template_folder="templates",
)

@user_crud.route("/")
def index():
    users = Users.query.all()
    return render_template("index.html", users=users)