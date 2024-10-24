def sum_of_list(numbers):
    total = 0  
    for num in numbers:
        total += num  
    return total

numbers = [10, 20, 30, 40, 50]

manual_sum = sum_of_list(numbers)
print(f"Sum using loop: {manual_sum}")

builtin_sum = sum(numbers)
print(f"Sum using built-in function: {builtin_sum}")
