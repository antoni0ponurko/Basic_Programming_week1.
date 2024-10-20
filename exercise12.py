months = ["January", "Fabruary,", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

which_month = int(input("Which month? "))

if which_month > 12 or which_month < 1:
    print("Pick a valid month! ")
else:
    print(f"The corresponding month is : {"which_month"-1}")
