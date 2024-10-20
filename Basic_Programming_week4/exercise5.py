# Create one list with the days of the week. Use the print command to print the following output in one
# line of code:
# - just the working days of the week
# - just the weekend days of the week
# - the unpaired days of the week
# - the paired days of the week
# Hint: what technique did we see last week to retrieve a part from a string?
# [‘Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# ['Saturday', 'Sunday’]
# ['Monday', 'Wednesday', 'Friday', 'Sunday']
# ['Tuesday', 'Thursday', 'Saturday']

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

print(days[:5])
print(days[-2:])
print(days[0:7:2])
print(days[1:7:2])
