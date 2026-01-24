from flask import Blueprint, render_template, request

from utils import (
    get_airports,
    get_flight_data,
    get_flights,
    get_passport_data,
)


airport_bp = Blueprint("airport", __name__)


@airport_bp.route("/airport", methods=["GET", "POST"])
def airport():
    airports = get_airports()
    if request.method == "GET":
        return render_template(
            "airport/flights.html",
            data=None,
            airports=airports,
        )

    if request.method == "POST":
        prev_values = {
            "origin": int(request.form.get("origin"))
            if request.form.get("origin")
            else None,
            "destination": int(request.form.get("destination"))
            if request.form.get("destination")
            else None,
            "date": request.form.get("date"),
        }
        data = get_flights(prev_values)
        print("DATA", data)
        return render_template(
            "airport/flights.html",
            prev_values=prev_values,
            data=data,
            airports=airports,
        )


@airport_bp.route("/airport/lookup", methods=["GET", "POST"])
def airport_lookup():
    if request.method == "GET":
        return render_template("airport/airport_lookup.html", data=None)

    if request.method == "POST":
        prev_values = {
            "table": request.form.get("table"),
            "string": int(request.form.get("string")),
        }
        if prev_values["table"] == "flight":
            data = get_flight_data(prev_values)
            return render_template(
                "airport/lookup_flight_results.html",
                prev_values=prev_values,
                data=data,
            )
        else:
            data = get_passport_data(prev_values)
            print("DATA", data)
            return render_template(
                "airport/airport_lookup.html",
                prev_values=prev_values,
                data=data,
            )

