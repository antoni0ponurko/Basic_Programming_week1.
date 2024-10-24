def generate_password_bis():
    letters = "abc"
    password_length = 6
    password = ''

    for i in range(password_length):
        index = (i * 3) % len(letters)
        password += letters[index]

    return password


password = generate_password_bis()

print(f"Your password is: {password}")
