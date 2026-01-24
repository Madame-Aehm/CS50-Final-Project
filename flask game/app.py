# python -m flask --app app run

# .venv/Scripts/activate
# cd "flask game"
# python -m flask --app app run --debug

from flask import Flask, render_template
from dotenv import load_dotenv
from routes import register_blueprints

load_dotenv()

app = Flask(__name__)

# Register all feature blueprints
register_blueprints(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", message=e)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/map")
def map():
    return render_template("map.html")