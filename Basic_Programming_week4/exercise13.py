def count_elements_within_interval(lst, min_val, max_val):
    count = 0

    for element in lst:

        if min_val <= element <= max_val:
            count += 1
    return count


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']


min_value1 = 40
max_value1 = 100
count1 = count_elements_within_interval(list1, min_value1, max_value1)

print(f"The number of elements between {
      min_value1} and {max_value1} is: {count1}")


min_value2 = 'a'
max_value2 = 'e'
count2 = count_elements_within_interval(list2, min_value2, max_value2)

print(f"The number of elements between {
      min_value2} and {max_value2} is: {count2}")
