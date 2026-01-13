# python -m flask --app app run

# .venv/Scripts/activate
# cd "flask game"
# python -m flask --app app run --debug

from flask import Flask, render_template, request, redirect
from utils import get_police_reports, get_police_interviews
from dotenv import load_dotenv

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
        return render_template("police_station.html", prev_values=None, reportData=None, interviewsData=None)
    if request.method == "POST":
        try:
            prev_values = {
                "date": request.form.get("date"), 
                "string": request.form.get("string"),
                "table": request.form.get("table")
            }
            if prev_values["table"] == "reports":
                data = get_police_reports(prev_values)
                return render_template("police_station.html",
                    prev_values=prev_values,
                    reportData=data)
            else:
                data = get_police_interviews(prev_values)
                return render_template("police_station.html",
                    prev_values=prev_values,
                    interviewsData=data)
        except:
            print("exception")
            return render_template("police_station.html",
                prev_values=prev_values)



# @app.route("/get-reports", methods=["POST"])
# def get_reports():
#     date = request.form.get("report-date")
#     if date: 
#         year, month, day = date.split("-")
#     street = request.form.get("street")
#     supabase = create_client(
#             os.getenv("SUPABASE_URL"), 
#             os.getenv("SUPABASE_KEY"))
#     if date and street:
#         response = (supabase.table("crime_scene_reports")
#             .select()
#             .eq("street", street)  
#             .eq("day", int(day))
#             .eq("month", int(month))
#             .eq("year", int(year))
#             .execute()
#         )
#     elif date:
#         response = (supabase.table("crime_scene_reports")
#             .select()  
#             .eq("day", int(day))
#             .eq("month", int(month))
#             .eq("year", int(year))
#             .execute()
#         )
#     elif street:
#         response = (supabase.table("crime_scene_reports")
#             .select().eq("street", street).execute()
#         )
#     else:
#         response = (supabase.table("crime_scene_reports").select().execute())
#     return render_template("police_station.html",
#         prev_values={"report-date": date, "street": street},
#         reportData=response.data)
    # else: 
    #     message = f"""
    #         All values are required.
    #         {validate_values([
    #             ("date", date), 
    #             ("street", street)])}
    #     """
    #     return render_template("error.html", message=message)

# @app.route("/get-interviews", methods=["POST"])
# def get_interviews():
#     date = request.form.get("date")
#     if date: 
#         year, month, day = date.split("-")
#     keyword = request.form.get("keyword")
#     supabase = create_client(
#         os.getenv("SUPABASE_URL"), 
#         os.getenv("SUPABASE_KEY"))
#     if date and keyword:
#         response = (supabase.table("interviews")
#             .select() 
#             .eq("day", int(day))
#             .eq("month", int(month))
#             .eq("year", int(year))
#             .like("transcript", f"%{keyword}%")
#             .execute()
#         )
#     elif date:
#         response = (supabase.table("interviews")
#             .select()  
#             .eq("day", int(day))
#             .eq("month", int(month))
#             .eq("year", int(year))
#             .execute()
#         )
#     elif keyword:
#         response = (supabase.table("interviews")
#             .select() 
#             .like("transcript", f"%{keyword}%")
#             .execute())
#     else:
#         response = (supabase.table("interviews").select().execute())
#     return render_template("police_station.html",
#         prev_values={"interviews-date": date, "keyword": keyword},
#         interviewsData=response.data)