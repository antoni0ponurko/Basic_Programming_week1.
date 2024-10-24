from datetime import datetime

year = int(input("What is your year of birth?"))
month = str(input("What month were you born"))

year_now = datetime.now().year
month_now = datetime.now().month

if year_now - year >= 18:
    print("Yay, you are older than 18 you can drink alcohol.")

else:
    print("I am sorry, you are too young, come back later.")
