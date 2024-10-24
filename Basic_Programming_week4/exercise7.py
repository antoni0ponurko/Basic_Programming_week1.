whole_numbers = [12, 45, -9, -15]
decimal_numbers = [12.23, 45.1, 9.478, 15.125, -3.14]
string_list = ["Joerie", "Marie", "Henk"]

def get_info_list(collection_name, collection):
    result = f"Collection {collection_name}\n"
    
    for index, element in enumerate(collection):
        result += f"{element} is on position {index}\n"
    return result

print(get_info_list("Non-decimal numbers", whole_numbers))
print(get_info_list("Decimal numbers", decimal_numbers))
print(get_info_list("Strings", string_list))
