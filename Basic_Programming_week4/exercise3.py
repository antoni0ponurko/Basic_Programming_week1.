# Create an empty list ‘friends’. We let the application dynamically expand this list. Each time, the user
# enters a new name or an empty string. In the latter case, the application stops by printing the list of
# friends.
friend = input(str("Enter a friends name, or exit with an empy field:>"))

friends_list = []

while friend != '':
    friends_list.append(friend)
    friend = input("Enter a friend's name or exit an empty field: ")
    print(f"My friends are: {friends_list}")
