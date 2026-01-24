from flask import Blueprint, render_template, request

from utils import get_atm_transactions, get_bank_accounts


bank_bp = Blueprint("bank", __name__)


@bank_bp.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "GET":
        return render_template("bank/bank_atm.html", data=None)

    if request.method == "POST":
        prev_values = {
            "date": request.form.get("date"),
            "location": request.form.get("location"),
            "transaction": request.form.get("transaction"),
        }
        data = get_atm_transactions(prev_values)
        print("DATA", data)
        return render_template(
            "bank/bank_atm.html",
            prev_values=prev_values,
            data=data,
        )


@bank_bp.route("/bank/accounts", methods=["GET", "POST"])
def bank_accounts():
    if request.method == "GET":
        return render_template("bank/bank_account.html", data=None)

    if request.method == "POST":
        prev_values = {
            "account_number": request.form.get("account_number"),
        }
        if not prev_values["account_number"]:
            return render_template(
                "error.html",
                message="Account number is required",
            )
        data = get_bank_accounts(prev_values)
        print("DATA", data)
        return render_template(
            "bank/bank_account.html",
            prev_values=prev_values,
            data=data[0] if data else None,
        )

