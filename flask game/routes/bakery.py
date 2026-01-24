from flask import Blueprint, render_template, request

from utils import get_security_logs


bakery_bp = Blueprint("bakery", __name__)


@bakery_bp.route("/bakery", methods=["GET", "POST"])
def bakery():
    if request.method == "GET":
        return render_template("bakery.html", data=None)

    if request.method == "POST":
        prev_values = {
            "from": request.form.get("from"),
            "to": request.form.get("to"),
            "date": request.form.get("date"),
        }
        if prev_values["from"] and prev_values["to"]:
            if prev_values["from"] > prev_values["to"]:
                return render_template(
                    "error.html",
                    message='"To" value must be less than "From"',
                )
        data = get_security_logs(prev_values)
        print("DATA", data)
        return render_template(
            "bakery.html",
            prev_values=prev_values,
            data=data,
        )

