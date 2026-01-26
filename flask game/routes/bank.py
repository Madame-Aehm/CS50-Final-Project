from flask import Blueprint, render_template, request

from forms import BankATMForm, BankAccountForm
from utils import get_atm_transactions, get_bank_accounts


bank_bp = Blueprint("bank", __name__)


@bank_bp.route("/bank", methods=["GET", "POST"])
def bank():
    form = BankATMForm()
    
    if request.method == "GET":
        return render_template("bank/bank_atm.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "date": form.date.data.isoformat() if form.date.data else None,
                "location": form.location.data.strip(),
                "transaction": form.transaction.data,
            }
            data = get_atm_transactions(prev_values)
            print("DATA", data)
            return render_template(
                "bank/bank_atm.html",
                form=form, data=data)
        else:
            return render_template("bank/bank_atm.html", form=form, data=None)


@bank_bp.route("/bank/accounts", methods=["GET", "POST"])
def bank_accounts():
    form = BankAccountForm()
    
    if request.method == "GET":
        return render_template("bank/bank_account.html", form=form, data=None)

    if request.method == "POST":
        if form.validate_on_submit():
            prev_values = {
                "account_number": form.account_number.data,
            }
            data = get_bank_accounts(prev_values)
            print("DATA", data)
            return render_template(
                "bank/bank_account.html",
                form=form, data=data)
        else:
            return render_template("bank/bank_account.html", form=form, data=None)

