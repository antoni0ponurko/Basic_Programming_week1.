def average_of_list(numbers):

    if len(numbers) == 0:
        return "-"

    else:
        total = sum(numbers)
        average = total / len(numbers)
        return round(average, 2)


list1 = [12, 45, 465, 78, 1, 23, 89]
list2 = []

print(f"Average of list1: {average_of_list(list1)}")

print(f"Average of list2: {average_of_list(list2)}")
