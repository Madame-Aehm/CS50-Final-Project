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
        if date and street:
            
            response = (supabase.table("crime_scene_reports")
                .select("*")
                .ilike("street", f"%{street}%")
                .eq("day", int(day))
                .eq("month", int(month))
                .eq("year", int(year))
                .execute())
        elif date:
            response = (supabase.table("crime_scene_reports")
                .select()  
                .eq("day", int(day))
                .eq("month", int(month))
                .eq("year", int(year))
                .execute())
        elif street:
            response = (supabase.table("crime_scene_reports")
                .select().ilike("street", f"%{street}%").execute())
        else:
            response = (supabase.table("crime_scene_reports").select().execute())
        return escape_strings(response.data, "description")


def get_police_interviews(form):
    date = form["date"]
    if date: 
        year, month, day = date.split("-")
    keyword = form["string"]
    supabase = create_client(
        os.getenv("SUPABASE_URL"), 
        os.getenv("SUPABASE_KEY"))
    if date and keyword:
        response = (supabase.table("interviews")
            .select() 
            .ilike("transcript", f"%{keyword}%")
            .eq("day", int(day))
            .eq("month", int(month))
            .eq("year", int(year))
            .execute()
        )
    elif date:
        response = (supabase.table("interviews")
            .select()  
            .eq("day", int(day))
            .eq("month", int(month))
            .eq("year", int(year))
            .execute()
        )
    elif keyword:
        response = (supabase.table("interviews")
            .select() 
            .ilike("transcript", f"%{keyword}%")
            .execute())
    else:
        response = (supabase.table("interviews").select().execute())
    return escape_strings(response.data, "transcript")


def get_security_logs(form):
    # filter_values = {}
    date = form["date"]
    if date: 
        year, month, day = date.split("-")
        # for i in enumerate(date.split("-")):
        #     filter
    from_time = form["from"]
    if from_time:
        from_time_hour, from_time_min = from_time.split(":")
    to_time = form["to"]
    if to_time:
        to_time_hour, to_time_min = to_time.split(":")
    supabase = create_client(
        os.getenv("SUPABASE_URL"), 
        os.getenv("SUPABASE_KEY"))
    if date and from_time and to_time:
        response = (supabase.table("bakery_security_logs")
            .select() 
            .eq("day", int(day))
            .eq("month", int(month))
            .eq("year", int(year))
            .lte("hour", to_time_hour)
            .lte("minute", to_time_min)
            .gte("hour", from_time_hour)
            .gte("minute", from_time_min)
            .execute()
        )
    else: response = None
    return response.data