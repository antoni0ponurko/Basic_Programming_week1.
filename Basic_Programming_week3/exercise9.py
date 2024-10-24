from random import randint

random_number = randint(1, 20)
print(random_number)
counter = 1

guess = int(input("Guess a number between 1 and 20: "))

while guess != random_number:
    if guess < random_number:
        print("The is too low. ")
else:
    print("The number is too big.")
    guess = int(input("Guess a number between  1 and 20: "))
    counter = counter + 1

    print(f"Right with {counter} attempts")
