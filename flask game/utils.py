from supabase import create_client
import os


def validate_values(values):
    missing_values = []
    for value in values:
        if bool(value[1]) == False:
            missing_values.append(value[0])
    if len(missing_values) > 0:
        if len(missing_values) > 1:
            missing_values[-1] = f"and {missing_values[-1]}"
        return f"Missing values: {", ".join(missing_values)}."
    return ""


def escape_strings(list, pos):
    for i in range(0, len(list)):
        list[i][pos] = list[i][pos].replace("'", "’")
    return list


def get_police_reports(form):
        date = form["date"]
        if date: 
            year, month, day = date.split("-")
        street = form["string"]
        supabase = create_client(
            os.getenv("SUPABASE_URL"), 
            os.getenv("SUPABASE_KEY"))
        query = supabase.table("crime_scene_reports").select()
        if date:
            (query.eq("day", int(day))
                .eq("month", int(month))
                .eq("year", int(year)))
        if street:
            query.ilike("street", f"%{street}%").execute()
        response = query.execute()
        # return escape_strings(response.data, "description")
        return response.data


def get_police_interviews(form):
    date = form["date"]
    if date: 
        year, month, day = date.split("-")
    keyword = form["string"]
    supabase = create_client(
        os.getenv("SUPABASE_URL"), 
        os.getenv("SUPABASE_KEY"))
    query = supabase.table("interviews").select()
    if date:
        (query.eq("day", int(day))
            .eq("month", int(month))
            .eq("year", int(year)))
    if keyword:
        query.ilike("transcript", f"%{keyword}%")
    response = query.execute()
    # return escape_strings(response.data, "transcript")
    return response.data


def get_security_logs(form):
    print("THIS IS FORM", form)
    date = form["date"]
    from_time = form["from"]
    to_time = form["to"]
    supabase = create_client(
        os.getenv("SUPABASE_URL"), 
        os.getenv("SUPABASE_KEY"))
    query = supabase.table("bakery_security_logs").select()
    if date:
        query.eq("date", date)
    if from_time:
        query.gte("time", from_time)
    if to_time:
        query.lte("time", to_time)
    response = query.execute()
    return response.data
