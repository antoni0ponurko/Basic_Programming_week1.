import random


def choose_random_element(collection):
    return random.choice(collection)


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

numbers = [100, 200, 300, 400, 500]

chosen_month = choose_random_element(months)
print("The chosen month is", chosen_month)

chosen_number = choose_random_element(numbers)
print("The selected number is", chosen_number)
