from flask import Flask

from .example_bp import example_bp

app = Flask(__name__)
app.register_blueprint(example_bp)

if __name__ == "__main__":
    app.run()
