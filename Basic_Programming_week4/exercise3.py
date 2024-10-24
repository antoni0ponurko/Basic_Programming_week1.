friends = []

while True:
    name = input("Enter a friend's name, or exit with an empty field:> ")
    
    if name == "":
        break 
    
    friends.append(name)

print("Your friends are", friends)
