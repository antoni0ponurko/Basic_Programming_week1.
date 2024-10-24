start_value = int(input("Enter a start value : "))
stop_value = int(input("Enter a stop value : "))

print(f"The numbers you are looking for between {
    start_value} and {stop_value}")
for i in range(start_value, stop_value+1):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
