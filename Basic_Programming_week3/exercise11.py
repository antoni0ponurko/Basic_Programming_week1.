start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

year = start_year


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    else:

        return False


while year <= end_year:
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    year += 1
