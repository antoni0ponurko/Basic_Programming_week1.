days = int(input("Enter the number of days: "))
hours = int(input("Enter the amount of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds

print(f"The total number of seconds: {total_seconds}")
