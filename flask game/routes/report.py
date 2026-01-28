from flask import Blueprint, render_template, request

from forms import ReportForm
from utils import identify_culprit


report_bp = Blueprint("report", __name__)


@report_bp.route("/report", methods=["GET", "POST"])
def bakery():
    form = ReportForm()
    
    if request.method == "GET":
        return render_template("report.html.j2", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "thief_name": form.thief_name.data.strip(),
                "city": form.city.data.strip(),
                "accomplice": form.accomplice.data.strip(),
            }
            data = identify_culprit(prev_values)
            print("DATA", data)
            return render_template("report.html.j2", form=form, data=data)
        else:
            return render_template("report.html.j2", form=form, data=None)

