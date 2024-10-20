# Program the function ‘max_en_min_uit_list’ with one parameter (a list). The function looks for the
# maximum and minimum from that list and returns both in one string. Test with a list of numbers and a
# list of words.
# From [11, 52, 125, -89, 1245] is the max: 1245 and min: -89
# From ['jan', 'feb', 'mar', 'apr', 'may'] is the max: may and min: apr

list_numbers = [11, 52, 125, -89, 1245]
list_month = ['jan', 'feb', 'mar', 'apr', 'may']


def max_and_min_from_list(my_list: list[object]) -> str:
    return f"(my_list) is the maximum : {max(my_list)} and the minimum : {min(my_list)}"


print(max_and_min_from_list(list_numbers))
print(max_and_min_from_list(list_month))
