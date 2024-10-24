from datetime import datetime

hour = datetime.now().hour


def show_message(hour, firstname):
    if hour < 12:
        return f"Good morning, {firstname}."
    elif hour < 18:
        return f"Good afternoon, {firstname}."
    else:
        return f"Good evening, {firstname}."


firstname = input("What is your first name? ")
welcome = show_message(hour, firstname)

print(welcome)
