def give_common_elements(list1, list2):

    common_elements = set(list1) & set(list2)

    return sorted(common_elements)


list1_numbers = [78, 4, 5, 6, 4]
list2_numbers = [89, 78, 4]

common_numbers = give_common_elements(list1_numbers, list2_numbers)

print(f"Common elements: {common_numbers}")


list3_words = ['Tamara', 'Delfien', 'Elke', 'Marijn']
list4_words = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']

common_words = give_common_elements(list3_words, list4_words)

print(f"Common elements: {common_words}")
