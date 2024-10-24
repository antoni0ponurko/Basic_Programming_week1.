workers = []
clerks = []
managers = []

num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    employee_type = input(f"Specify the type of employee {i + 1} (W: Worker, C: Clerk, M: Manager): ").upper()
    salary = float(input("Enter the salary: "))
    
    if employee_type == 'W':
        workers.append(salary)
    
    elif employee_type == 'C':
        clerks.append(salary)
    
    elif employee_type == 'M':
        managers.append(salary)
    
    else:
        print("Invalid employee type. Please enter W, C, or M.")

print("\nOverview:")

for salary in workers:
    print(f"W {salary}€")

for salary in clerks:
    print(f"C {salary}€")

for salary in managers:
    print(f"M {salary}€")

total_employees = len(workers) + len(clerks) + len(managers)
total_cost = sum(workers) + sum(clerks) + sum(managers)


print(f"\nTotal number of employees: {total_employees}")
print(f"Number of workers: {len(workers)}")
print(f"Number of clerks: {len(clerks)}")
print(f"Number of managers: {len(managers)}")
print(f"Total cost: {total_cost}€")
