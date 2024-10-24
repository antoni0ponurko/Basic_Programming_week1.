def car_rental():

    car_types = {
        'A': {'fixed': 25, 'variable': 0.5},
        'B': {'fixed': 35, 'variable': 0.6},
        'C': {'fixed': 45, 'variable': 0.7},
    }

    total_revenue = 0
    revenue_by_type = {'A': 0, 'B': 0, 'C': 0}
    cars_rented_count = {'A': 0, 'B': 0, 'C': 0}
    kilometers_driven = {'A': 0, 'B': 0, 'C': 0}

    while True:

        car_type = input(
            "Enter car type (A, B, C) or 'exit' to finish: ").upper()
        if car_type == 'EXIT':
            break

        if car_type not in car_types:
            print("Invalid car type. Please enter A, B, or C.")
            continue

        days = int(input("Enter the number of days rented: "))
        kilometers = float(input("Enter the kilometers driven: "))

        fixed_cost = car_types[car_type]['fixed']
        variable_cost = car_types[car_type]['variable'] * kilometers
        total_cost = (fixed_cost * days) + variable_cost

        total_revenue += total_cost
        revenue_by_type[car_type] += total_cost

        cars_rented_count[car_type] += 1
        kilometers_driven[car_type] += kilometers

    print("\nSummary of Car Rental Revenue:")
    print(f"Total Revenue: €{total_revenue:.2f}")
    print(f"Revenue for type A cars: €{revenue_by_type['A']:.2f}")
    print(f"Revenue for type B cars: €{revenue_by_type['B']:.2f}")
    print(f"Revenue for type C cars: €{revenue_by_type['C']:.2f}")
    print(f"Total number of type A cars rented out: {cars_rented_count['A']}")
    print(f"Total number of type B cars rented out: {cars_rented_count['B']}")
    print(f"Total number of type C cars rented out: {cars_rented_count['C']}")
    print(f"Total kilometers driven")
