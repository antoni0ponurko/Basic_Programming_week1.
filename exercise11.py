# Функція для перевірки, чи рік високосний
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

year = start_year
while year <= end_year:
    if is_leap_year(year):  # type: ignore
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    year += 1


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    else:

        return False
