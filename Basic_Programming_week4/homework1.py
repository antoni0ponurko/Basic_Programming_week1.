def its_equal(list_a, list_b):
    return sorted(list_a) == sorted(list_b)


list_a = [10, 14, 2, 3, -10]
list_b = [-10, 3, 2, 10, 14]

print(f"Equal?: {its_equal(list_a, list_b)}")