# python -m flask --app app run
# python -m flask --app app run --debug

from flask import Flask, render_template, request, redirect
from utils import validate_values
from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()

app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", message=e)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/police-station", methods=["GET", "POST"])
def police_station():
    if request.method == "GET":
        return render_template("police_station.html")
    
    if request.method == "POST":
        if (request.form.get("id") == "reports"):
            day = request.form.get("day")
            month = request.form.get("month")
            year = request.form.get("year")
            street = request.form.get("street")
            if day and month and year and street:
                supabase = create_client(
                    os.getenv("SUPABASE_URL"), 
                    os.getenv("SUPABASE_KEY"))
                response = (supabase.table("crime_scene_reports")
                    .select()
                    .eq("street", street)  
                    .eq("day", int(day))
                    .eq("month", int(month))
                    .eq("year", int(year))
                    .execute()
                )
            else: 
                message = f"""
                All values are required.
                {validate_values([
                    ("day", day), 
                    ("month", month), 
                    ("year", year), 
                    ("street", street)])}
                """
                return render_template("error.html", message=message)
        return redirect("/police-station")
    
