def are_totally_different(list1, list2):

    for element in list1:

        if element in list2:
            return False
    return True


list1 = [4, 5, 6, 4]
list2 = [89, 78, 4]


if are_totally_different(list1, list2):
    print("List1 and List2 have no common elements.")

else:
    print("List1 and List2 have at least one common element.")
