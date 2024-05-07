from flask import Blueprint, render_template

example_bp = Blueprint("example_blueprint", __name__)


@example_bp.route("/")
def index():
    return render_template("index.html")
