last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
birth_date = input("Enter your date of birth (dd-mm-yyyy): ")


def generate_password(last_name, first_name, birth_date):

    part1 = last_name[:3].lower()

    part2 = first_name[:2].upper()

    day, month, year = birth_date.split('-')
    part3 = month + year[2:]

    password = part1 + part2 + part3
    return password


password = generate_password(last_name, first_name, birth_date)
print(password)
