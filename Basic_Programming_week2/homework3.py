def show_message(hour, firstname):

    if 7 <= hour < 12:
        return f"Good morning, {firstname}"

    elif hour == 12:
        return f"Yay, it's afternoon, {firstname}"

    elif 13 <= hour <= 16:
        return f"Good afternoon, {firstname}"

    elif 17 <= hour <= 20:
        return f"Good evening, {firstname}"

    else:
        return f"Good night, {firstname}"


hour = int(input(" What time is it? "))
firstname = input(" What is your first name? ")


welcome = show_message(hour, firstname)

print(welcome)
