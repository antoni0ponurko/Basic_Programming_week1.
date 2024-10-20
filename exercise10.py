categories = {
    "V": {"name": "Vegetables", "total_cost": 0, "count": 0},
    "F": {"name": "Fruit", "total_cost": 0, "count": 0},
    "B": {"name": "Beverages", "total_cost": 0, "count": 0}
}


def give_ticket_by_category(category_name, total_price, product_count):
    if product_count > 0:
        average_price = total_price / product_count
    else:
        average_price = 0
    return f"{product_count} products are in the category {category_name} " \
        f"Total cost: {total_price:.2f} " \
        f"Average price per product: {average_price:.2f}"


num_products = int(
    input("Specify the number of products you wish to enter:> "))


current_product = 0
while current_product < num_products:
    category = input(
        "What is the category? [V: Vegetables, F: Fruit, B: Beverages]> ").upper()
    price = float(input("What is the cost price of the product?> "))

    if category in categories:
        categories[category]["total_cost"] += price
        categories[category]["count"] += 1
        current_product += 1
    else:
        print("Invalid category. Try again.")


category_keys = list(categories.keys())
i = 0
while i < len(category_keys):
    category_key = category_keys[i]
    category_data = categories[category_key]
    print(give_ticket_by_category(
        category_data["name"], category_data["total_cost"], category_data["count"]
    ))
    i += 1
