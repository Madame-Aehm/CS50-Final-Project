from flask import Blueprint, render_template, request

from forms import AirportFlightsForm, AirportLookupForm
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
    form = AirportFlightsForm()
    
    # Populate choices dynamically
    airport_choices = [("", "Select")] + [(airport["id"], f"{airport['city']} ({airport['abbreviation']})") for airport in airports]
    form.origin.choices = airport_choices
    form.destination.choices = airport_choices
    
    if request.method == "GET":
        return render_template(
            "airport/flights.html",
            form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "origin": form.origin.data if form.origin.data else None,
                "destination": form.destination.data if form.destination.data else None,
                "date": form.date.data.isoformat() if form.date.data else None,
            }
            data = get_flights(prev_values)
            print("DATA", data)
            return render_template(
                "airport/flights.html",
                form=form, data=data)
        else:
            return render_template(
                "airport/flights.html",
                form=form,
                data=None
            )


@airport_bp.route("/airport/lookup", methods=["GET", "POST"])
def airport_lookup():
    form = AirportLookupForm()
    
    if request.method == "GET":
        return render_template("airport/airport_lookup.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "table": form.table.data,
                "string": form.string.data.strip(),
            }
            if prev_values["table"] == "flight":
                data = get_flight_data(prev_values)
                return render_template(
                    "airport/lookup_flight_results.html",
                    form=form, data=data)
            else:
                data = get_passport_data(prev_values)
                print("DATA", data)
                return render_template(
                    "airport/lookup_passport_results.html",
                    form=form, data=data)
        else:
            return render_template("airport/airport_lookup.html", form=form, data=None)

