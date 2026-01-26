from flask import Blueprint, render_template, request

from forms import PoliceStationForm
from utils import get_license_data, get_police_data


police_bp = Blueprint("police", __name__)


@police_bp.route("/police-station", methods=["GET", "POST"])
def police_station():
    form = PoliceStationForm()
    
    if request.method == "GET":
        return render_template(
            "police_station.html",
            form=form, data=None)

    if request.method == "POST":
        try:
            if form.validate_on_submit():
                prev_values = {
                    "date": form.date.data.isoformat() if form.date.data else None,
                    "string": form.string.data.strip(),
                    "table": form.table.data,
                }
                if prev_values["table"] == "reports":
                    data = get_police_data("crime_scene_reports", prev_values)
                    print("DATA", data)
                    return render_template(
                        "police/police_results_reports.html",
                        form=form, data=data)
                elif prev_values["table"] == "interviews":
                    data = get_police_data("interviews", prev_values)
                    print("DATA", data)
                    return render_template(
                        "police/police_results_interviews.html",
                        form=form, data=data)
                else:
                    data = get_license_data(prev_values)
                    print("DATA", data)
                    return render_template(
                        "police/police_results_lp.html",
                        form=form, data=data[0] if data else None)
            else:
                return render_template(
                    "police_station.html",
                    form=form, data=None)
        except Exception as e:
            print("error occurred: ", e)
            return render_template("error.html", message=e)

