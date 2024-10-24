name = input("What is your first name? ")
group_name = input("What is the name of the group? ")


def create_welcome_in_class(first_name: str, group: str = '1CTAI1') -> str:
    return f"Welcome {first_name} in {group}"


welcome_message = create_welcome_in_class('Anton', '1CTAI1')
print("welcome_message")
print(create_welcome_in_class('Anton'))
print(create_welcome_in_class(name, group_name))
