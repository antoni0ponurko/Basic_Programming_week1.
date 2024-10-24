unit = input("Which temperature unit are you using? [C:Celsius, F:Farenheit]")


def give_celsius(temp_farenheit: float) -> float:
    return (temp_farenheit-32) * 5/9


def give_farenheit(temp_celsius: float) -> float:
    return (temp_celsius*9/5)+32


if unit.upper() == 'C':
    temp = input("Give a temperaturte in celsius: ")
    temp_F = give_farenheit(temp)
    print(f"The corresponding temp in farenheit is: {temp_F}")
elif unit.upper() == 'F':
    temp = input("Give a temperature in Fareheit: ")
    temp_c = give_celsius(temp)
    print(f"The corresponding temp in celsius is: {temp_c}")
else:
    print("Give a valid temperature unit!!!!")
