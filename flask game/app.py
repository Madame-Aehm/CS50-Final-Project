# python -m flask --app app run

# .venv/Scripts/activate
# cd "flask game"
# python -m flask --app app run --debug

from flask import Flask, render_template, request, redirect
from utils import get_police_data, get_security_logs, get_atm_transactions
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


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


@app.route("/police-station", methods=["GET", "POST"])
def police_station():
    if request.method == "GET":
        return render_template("police_station.html", prev_values=None, reportData=None, interviewsData=None)
    if request.method == "POST":
        try:
            prev_values = {
                "date": request.form.get("date"), 
                "string": request.form.get("string"),
                "table": request.form.get("table")
            }
            if prev_values["table"] == "reports":
                data = get_police_data("crime_scene_reports", prev_values)
                return render_template("police_station.html",
                    prev_values=prev_values,
                    reportData=data)
            else:
                data = get_police_data("interviews", prev_values)
                return render_template("police_station.html",
                    prev_values=prev_values,
                    interviewsData=data)
        except:
            print("exception")
            return render_template("police_station.html",
                prev_values=prev_values)


@app.route("/bakery", methods=["GET", "POST"])
def bakery():
    if request.method == "GET":
        return render_template("bakery.html")
    if request.method == "POST":
        prev_values = {
            "from": request.form.get("from"),
            "to": request.form.get("to"),
            "date": request.form.get("date")
        }
        if prev_values["from"] and prev_values["to"]:
            if prev_values["from"] > prev_values["to"]:
                return render_template("error.html", message='"To" value must be less than "From"')
        data = get_security_logs(prev_values)
        print("DATA", data)
        return render_template("bakery.html", prev_values=prev_values, data=data)
    

@app.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "GET":
        return render_template("bank_atm.html")
    if request.method == "POST":
        prev_values = {
            "date": request.form.get("date"),
            "location": request.form.get("location"),
            "transaction": request.form.get("transaction")
        }
        data = get_atm_transactions(prev_values)
        print("DATA", data)
        return render_template("bank_atm.html", prev_values=prev_values, data=data)


@app.route("/bank/accounts", methods=["GET", "POST"])
def bank_accounts():
    if request.method == "GET":
        return render_template("bank_account.html")