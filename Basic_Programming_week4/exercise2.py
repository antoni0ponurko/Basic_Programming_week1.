new_list_numbers = []
new_list_numbers = list(range(1, 483, 13))
print(new_list_numbers)

new_list_numbers.reverse()
print(new_list_numbers)

new_list_numbers.remove(482)
print(new_list_numbers)

element_to_delete = 39
if element_to_delete in new_list_numbers:
    new_list_numbers.remove(element_to_delete)
    print(new_list_numbers)
