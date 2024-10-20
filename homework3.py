def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

print(f"Leap years between {start_year} and {end_year}:")

for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(f"{year} is a leap year")
