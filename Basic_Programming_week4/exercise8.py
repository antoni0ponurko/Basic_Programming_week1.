# Program the function ‘choose_random_element’ with one parameter (a list). The function chooses one
# random element from the list and returns that element. Test the function with
# - a list with the months
# - a list with numbers
# Hint: Use the documentation of the module Random: what are the different ways to look up a random
# value out a list?
# The chosen month is September
# The selected number is 200.

from random import choice

months = ["January", "February", "March", "April", "May"]
numbers = [1, 2, 3, 4, 5, 6]


def choose_random_element(my_list: list[object]) -> object:
    return choice(my_list)


print(choose_random_element(months))
print(choose_random_element(numbers))
