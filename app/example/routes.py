from flask import Blueprint, render_template

example_bp = Blueprint(
    "example_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/example/static",
)


@example_bp.route("/")
def index():
    return render_template("index.html")
