# Write a function 'remove_duplicates' that has a list as a parameter. This function will return a new list
# without duplicates. Test it by printing both lists.
# ['A', 89, 78, 4, 'A', 'test', 4]
# Without duplicates: ['A', 89, 78, 4, 'test']
def remove_duplicates(my_list: list[object]) -> object:
    without_dupl = []
    for elements in my_list:
        if elements not in without_dupl:
            without_dupl.append(elements)
            return without_dupl


test1 = ['A', 89, 78, 4, 'A', 'test', 4]
test = ['A', 89, 78, 4, 'test']

print(f"{test}\nWithout duplicates : {test}")
print(f"{test1}\nWithout duplicates : {test}")
