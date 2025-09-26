# python -m flask --app app run
# python -m flask --app app run --debug

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/police-station")
def police_station():
    return render_template("police_station.html")