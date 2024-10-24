# Ask the user to enter a temperature in Celsius. Make sure the user can enter a number with a decimal
# point. Now calculate the temperature in Fahrenheit and in Kelvin. Print both results (rounded to one
# digit).
# Fahrenheit = (Celsius × 9/5) + 32
# Kelvin = Celsius + 273.15

celsius = float(input("Enter a temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = (celsius + 273.15)


print(f"{celsius}C is equal to {round(fahrenheit, 1)}F and {round(kelvin, 1)}K")
