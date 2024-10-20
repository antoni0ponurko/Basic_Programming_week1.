def check_emailaddress(email):

    if "@student.howest.be" in email and "." in email.split("@")[0]:
        return True
    return False


email = input("Enter the email address: ")


if check_emailaddress(email):
    print("Valid student email address")
else:
    print("Invalid student email address")
