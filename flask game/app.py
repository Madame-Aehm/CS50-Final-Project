# python -m flask --app app run

# .venv/Scripts/activate
# cd "flask game"
# python -m flask --app app run --debug

from flask import Flask, render_template, request, redirect
from utils import get_police_data, get_security_logs, get_atm_transactions, get_bank_accounts, get_license_data
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
                print("DATA", data)
                return render_template("police_results_reports.html",
                    prev_values=prev_values,
                    data=data)
            elif prev_values["table"] == "interviews":
                data = get_police_data("interviews", prev_values)
                print("DATA", data)
                return render_template("police_results_interviews.html",
                    prev_values=prev_values,
                    data=data)
            else:
                if not prev_values["string"]:
                    return render_template("error.html", message="License plate number is required")
                data = get_license_data(prev_values)
                print("DATA", data)
                return render_template("police_results_lp.html", 
                    prev_values=prev_values,
                    data=data[0] if data else None)
        except Exception as e:
            print("error occurred: ", e)
            return render_template("error.html", message=e)


@app.route("/bakery", methods=["GET", "POST"])
def bakery():
    if request.method == "GET":
        return render_template("bakery.html", data=None)
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
        return render_template("bank_atm.html", data=None)
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
    if request.method == "POST":
        prev_values = {
            "account_number": request.form.get("account_number")
        }
        if not prev_values["account_number"]:
            return render_template("error.html", message="Account number is required")
        data = get_bank_accounts(prev_values)
        print("DATA", data)
        return render_template("bank_account.html", prev_values=prev_values, data=data[0] if data else None)