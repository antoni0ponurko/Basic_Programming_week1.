email = input("Enter an existing howest-email address: ")

name_part = email.split('@')[0]
first_name, last_name = name_part.split('.')


first_name = first_name.capitalize()
last_name = last_name.capitalize()


print(f"The last name is {last_name} and the first name is {first_name}")
