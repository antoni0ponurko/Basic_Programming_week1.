import random


def choose_5_numbers(min_value, max_value):

    unique_numbers = set()

    while len(unique_numbers) < 5:
        number = random.randint(min_value, max_value)

        unique_numbers.add(number)

    return list(unique_numbers)


min_value = int(input("Enter the minimum: "))
max_value = int(input("Enter the maximum: "))

selected_numbers = choose_5_numbers(min_value, max_value)

print(f"The five selected numbers in between are: {selected_numbers}")
