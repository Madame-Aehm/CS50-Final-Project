from flask import Blueprint, render_template, request

from forms import BakeryForm
from utils import get_security_logs


bakery_bp = Blueprint("bakery", __name__)


@bakery_bp.route("/bakery", methods=["GET", "POST"])
def bakery():
    form = BakeryForm()
    
    if request.method == "GET":
        return render_template("bakery.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "date": form.date.data.isoformat() if form.date.data else None,
                "from": form.from_field.data.strftime("%H:%M:%S") if form.from_field.data else None,
                "to": form.to_field.data.strftime("%H:%M:%S") if form.to_field.data else None,
            }
            data = get_security_logs(prev_values)
            print("DATA", data)
            return render_template(
                "bakery.html",
                form=form, data=data)
        else:
            return render_template("bakery.html", form=form, data=None)

