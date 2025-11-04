def validate_values(values):
    print("VALUES", values)
    missing_values = []
    for value in values:
        if bool(value[1]) == False:
            missing_values.append(value[0])
    print("MESSAGE AFTER LOOP", missing_values)
    if len(missing_values) > 0:
        if len(missing_values) > 1:
            missing_values[-1] = f"and {missing_values[-1]}"
        return f"Missing values: {", ".join(missing_values)}."
    return ""