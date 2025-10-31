# python -m flask --app app run
# python -m flask --app app run --debug

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/police-station", methods=["GET", "POST"])
def police_station():
    if request.method == "GET":
        return render_template("police_station.html")
    if request.method == "POST":
        if (request.form.get("id") == "reports"):
            day = request.form.get("day")
            month = request.form.get("month")
            year = request.form.get("year")
            street = request.form.get("street")
            if day and month and year and street:
                print("all values present")
            else: redirect("/police_station.html", report_error="All values must be specified")
        return redirect("/police-station")