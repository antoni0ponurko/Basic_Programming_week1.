# start value
# positive step
# amount -> use to calculate stop value
# function print_list_numbers(start, step, amount) -> None
# prints the numbers

start_value = int(input("Enter the start value : "))
step_value = int(input("Enter the positive step : "))
amount = int(input("Enter the amount of number to be printed : "))


def print_list_numbers(start: int, step: int, amount: int) -> None:
    stop = start + step*amount
    for i in range(start, stop+1, step):
        print(i)


print_list_numbers(start_value, step_value, amount)
