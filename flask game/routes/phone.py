from flask import Blueprint, render_template, request

from utils import get_call_history, phonebook_search


phone_bp = Blueprint("phone", __name__)


@phone_bp.route("/telephone", methods=["GET", "POST"])
def telephone():
    if request.method == "GET":
        return render_template("phone/phone_records.html", data=None)

    if request.method == "POST":
        prev_values = {
            "date": request.form.get("date"),
            "caller": request.form.get("caller"),
            "receiver": request.form.get("receiver"),
        }
        data = get_call_history(prev_values)
        print("DATA", data)
        return render_template(
            "phone/phone_records.html",
            prev_values=prev_values,
            data=data,
        )


@phone_bp.route("/telephone/book", methods=["GET", "POST"])
def telephone_book():
    if request.method == "GET":
        return render_template("phone/phone_book.html", data=None)

    if request.method == "POST":
        prev_values = {
            "search": request.form.get("search"),
            "query": request.form.get("query"),
        }
        data = phonebook_search(prev_values)
        print("DATA", data)
        return render_template(
            "phone/phone_book.html",
            prev_values=prev_values,
            data=data,
        )

