from database.supabase_client import get_supabase_client


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


def get_police_data(table, form):
    date = form["date"]
    if date: 
        year, month, day = date.split("-")
    supabase = get_supabase_client()
    query = supabase.table(table).select()
    if date:
        (query.eq("day", int(day))
            .eq("month", int(month))
            .eq("year", int(year)))
    if form["string"]:
        string_val = ("transcript" if table == "interviews" else "street")
        query.ilike(string_val, f"%{form["string"]}%")
    return query.execute().data


def get_security_logs(form):
    supabase = get_supabase_client()
    query = supabase.table("bakery_security_logs").select()
    if form["date"]:
        query.eq("date", form["date"])
    if form["from"]:
        query.gte("time", form["from"])
    if form["to"]:
        query.lte("time", form["to"])
    return query.execute().data


def get_atm_transactions(form):
    supabase = get_supabase_client()
    query = supabase.table("atm_transactions").select()
    if form["date"]:
        query.eq("date", form["date"])
    if form["location"]:
        query.ilike("atm_location", f"%{form["location"]}%")
    if form["transaction"]:
        query.eq("transaction_type", form["transaction"])
    return query.execute().data


def get_bank_accounts(form):
    supabase = get_supabase_client()
    query = (supabase.table('bank_accounts')
        .select('*, people(*)')
        .eq('account_number', form['account_number']))
    return query.execute().data


def get_license_data(form):
    supabase = get_supabase_client()
    query = supabase.table("people").select().eq("license_plate", form["string"])
    return query.execute().data


def get_call_history(form):
    supabase = get_supabase_client()
    query = supabase.table("phone_calls").select()
    if form["date"]:
        query.eq("date", form["date"])
    if form["caller"]:
        query.eq("caller", form["caller"])
    if form["receiver"]:
        query.eq("receiver", form["receiver"])
    return query.execute().data


def phonebook_search(form):
    supabase = get_supabase_client()
    query = (supabase.table("people").select()
        .ilike(form["search"], f"%{form["query"]}%"))
    return query.execute().data


def get_airports():
    supabase = get_supabase_client()
    query = supabase.table("airports").select()
    return query.execute().data


def get_flights(form):
    supabase = get_supabase_client()
    query = (supabase.table("flights")
        .select('*, origin_airport_id(*), destination_airport_id(*)'))
    if form["date"]:
        query.eq("date", form["date"])
    if form["origin"]:
        query.eq("origin_airport_id", form["origin"])
    if form["destination"]:
        query.eq("destination_airport_id", form["destination"])
    return query.execute().data


def get_flight_data(form):
    supabase = get_supabase_client()
    query = (supabase.table("passengers").select()
        .eq("flight_id", form["string"]))
    return query.execute().data


def get_passport_data(form):
    supabase = get_supabase_client()
    query = (supabase.table("people").select()
        .eq("passport_number", form["string"]))
    return query.execute().data