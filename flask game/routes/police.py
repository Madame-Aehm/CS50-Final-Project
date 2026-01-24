from flask import Blueprint, render_template, request

from utils import get_license_data, get_police_data


police_bp = Blueprint("police", __name__)


@police_bp.route("/police-station", methods=["GET", "POST"])
def police_station():
    if request.method == "GET":
        return render_template(
            "police_station.html",
            prev_values=None,
            reportData=None,
            interviewsData=None,
        )

    if request.method == "POST":
        try:
            prev_values = {
                "date": request.form.get("date"),
                "string": request.form.get("string"),
                "table": request.form.get("table"),
            }
            if prev_values["table"] == "reports":
                data = get_police_data("crime_scene_reports", prev_values)
                print("DATA", data)
                return render_template(
                    "police/police_results_reports.html",
                    prev_values=prev_values,
                    data=data,
                )
            elif prev_values["table"] == "interviews":
                data = get_police_data("interviews", prev_values)
                print("DATA", data)
                return render_template(
                    "police/police_results_interviews.html",
                    prev_values=prev_values,
                    data=data,
                )
            else:
                if not prev_values["string"]:
                    return render_template(
                        "error.html",
                        message="License plate number is required",
                    )
                data = get_license_data(prev_values)
                print("DATA", data)
                return render_template(
                    "police/police_results_lp.html",
                    prev_values=prev_values,
                    data=data[0] if data else None,
                )
        except Exception as e:
            print("error occurred: ", e)
            return render_template("error.html", message=e)

