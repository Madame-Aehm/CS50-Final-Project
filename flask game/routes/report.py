from flask import Blueprint, render_template, request

from utils import identify_culprit


report_bp = Blueprint("report", __name__)


@report_bp.route("/report", methods=["GET", "POST"])
def bakery():
    if request.method == "GET":
        return render_template("report.html", data=None)

    if request.method == "POST":
        prev_values = {
            "thief_name": request.form.get("thief_name"),
            "city": request.form.get("city"),
            "accomplice": request.form.get("accomplice"),
        }
        data = identify_culprit(prev_values)
        print("DATA", data)
        return render_template(
            "report.html",
            prev_values=prev_values,
            data=data,
        )

