# a list with 4 whole numbers
# - a list with 5 decimals
# - a list with 3 string
collection1 = [1, 2, 3, 4]
collection2 = [1.2, 2.5, 4.6]
collection3 = ["Name", "Dog", "Cat"]


def get_info_list(list_name: str, my_list: list[object]) -> str:
    s = f"Collection {list_name}\n"
    i = 0
    for element in my_list:
        s = s + f"{element} is on position {i}"
        return s

    print(get_info_list("Non-decimal numbers", collection1))
