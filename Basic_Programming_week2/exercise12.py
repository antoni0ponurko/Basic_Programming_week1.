month = input("What month is it? ")


def translate_month_number_to_string(month_number: int) -> str:
    if month_number == 1:
        return f"The corresponding month is January"
    elif month_number == 2:
        return f"The corresponding month is February"
    elif month_number == 3:
        return f"The corresponding month is March"
    elif month_number == 4:
        return f"The corresponding month is April"
    elif month_number == 5:
        return f"The corresponding month is May"
    elif month_number == 6:
        return f"The corresponding month is June"
    elif month_number == 7:
        return f"The corresponding month is July"
    elif month_number == 8:
        return f"The corresponding month is August"
    elif month_number == 9:
        return f"The corresponding month is September"
    elif month_number == 10:
        return f"The corresponding month is October"
    elif month_number == 11:
        return f"The corresponding month is November"
    elif month_number == 12:
        return f"The corresponding month is  December"
    else:
        return f"Invalid number"


print(translate_month_number_to_string)
