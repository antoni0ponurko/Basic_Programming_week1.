email = input("Enter an existing howest-email address: ")

name_part = email[:email.index('@')]

dot_index = name_part.index('.')
first_name = name_part[:dot_index]
last_name = name_part[dot_index + 1:]


first_name = first_name[0].upper() + first_name[1:]
last_name = last_name[0].upper() + last_name[1:]


print(f"The last name is {last_name} and the first name is {first_name}")
