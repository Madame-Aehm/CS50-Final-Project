from flask import Blueprint, render_template, request

from forms import PhoneRecordsForm, PhoneBookForm
from utils import get_call_history, phonebook_search


phone_bp = Blueprint("phone", __name__)


@phone_bp.route("/telephone", methods=["GET", "POST"])
def telephone():
    form = PhoneRecordsForm()
    
    if request.method == "GET":
        return render_template("phone/phone_records.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "date": form.date.data.isoformat() if form.date.data else None,
                "caller": form.caller.data.strip(),
                "receiver": form.receiver.data.strip(),
            }
            data = get_call_history(prev_values)
            print("DATA", data)
            return render_template(
                "phone/phone_records.html",
                form=form, data=data)
        else:
            return render_template("phone/phone_records.html", form=form, data=None)


@phone_bp.route("/telephone/book", methods=["GET", "POST"])
def telephone_book():
    form = PhoneBookForm()
    
    if request.method == "GET":
        return render_template("phone/phone_book.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "search": form.search.data,
                "query": form.query.data.strip(),
            }
            data = phonebook_search(prev_values)
            print("DATA", data)
            return render_template(
                "phone/phone_book.html",
                form=form, data=data)
        else:
            return render_template("phone/phone_book.html", form=form, data=None)

