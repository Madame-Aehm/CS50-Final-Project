from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    SelectField,
    IntegerField,
)
from wtforms.validators import InputRequired, Optional, ValidationError


def validate_time_range(form, field):
    """Custom validator to ensure 'from' time is less than 'to' time"""
    if form.from_field.data and form.to_field.data:
        if form.from_field.data >= form.to_field.data:
            raise ValidationError('"From" value must be less than "To" value')


def validate_license_plate_required(form, field):
    """Custom validator to require string when table is lp_lookup"""
    if form.table.data == "lp_lookup" and not field.data:
        raise ValidationError("License plate number is required")


class PoliceStationForm(FlaskForm):
    table = SelectField(
        "Search:",
        choices=[
            ("reports", "Police Reports"),
            ("interviews", "Police Interviews"),
            ("lp_lookup", "License Plate Lookup"),
        ],
        validators=[InputRequired()],
    )
    date = DateField("Date:", validators=[Optional()])
    string = StringField(
        "String:", 
        validators=[Optional(), validate_license_plate_required], 
        render_kw={"max": "2024-08-01", "min": "2024-01-01"})


class BankATMForm(FlaskForm):
    date = DateField(
        "Date:", 
        validators=[Optional()],
        render_kw={"min": "2024-07-26", "max": "2024-08-01"})
    location = StringField("Location:", validators=[Optional()])
    transaction = SelectField(
        "Transaction type:",
        choices=[("", "Select"), ("deposit", "Deposit"), ("withdraw", "Withdraw")],
        validators=[Optional()],
    )


class BankAccountForm(FlaskForm):
    account_number = IntegerField("Account Number:", validators=[InputRequired()])


class BakeryForm(FlaskForm):
    date = DateField(
        "Date:", 
        validators=[Optional()], 
        render_kw={"min": "2024-07-25", "max": "2024-07-31"})
    from_field = TimeField("From:", validators=[Optional(), validate_time_range])
    to_field = TimeField("To:", validators=[Optional()])


class AirportFlightsForm(FlaskForm):
    date = DateField("Date:", validators=[Optional()])
    origin = SelectField("Origin:", validators=[Optional()], choices=[])
    destination = SelectField("Destination:", validators=[Optional()], choices=[])


class AirportLookupForm(FlaskForm):
    table = SelectField(
        "Search:",
        choices=[("flight", "Flight"), ("passport", "Passport")],
        validators=[InputRequired()],
    )
    string = IntegerField("String:", validators=[InputRequired()])


class PhoneRecordsForm(FlaskForm):
    date = DateField(
        "Date:", 
        validators=[Optional()],
        render_kw={"min": "2024-07-25", "max": "2024-07-31"})
    caller = StringField("Caller:", validators=[Optional()])
    receiver = StringField("Receiver:", validators=[Optional()])


class PhoneBookForm(FlaskForm):
    search = SelectField(
        "Search:",
        choices=[("name", "Name"), ("phone_number", "Phone Number")],
        validators=[InputRequired()],
    )
    query = StringField("Query:", validators=[InputRequired()])


class ReportForm(FlaskForm):
    thief_name = StringField("Thief Name:", validators=[Optional()])
    city = StringField("City the Thief Escaped To:", validators=[Optional()])
    accomplice = StringField("Thief's Accomplice:", validators=[Optional()])
