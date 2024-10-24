from datetime import datetime

dog_age = int(input("What is your dogs age"))

if dog_age < 0:
    print("Your dog cannot be less than 0 years old!")

elif dog_age == 1:
    print("Your dog is 14 in human years")

elif dog_age == 2:
    print("Your dog is 22 in human years")

else:
    print("This age is equivalent to {22+(dao_age-2)*5}")
