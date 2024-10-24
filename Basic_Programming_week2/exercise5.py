import math

score = float(input("Enter your score: "))

rounded_score = math.floor(score + 0.5)

if rounded_score >= 10:
    print("Congratulations, you passed!")
else:
    print("Alas, better luck next time!")

print("Your rounded score is:", rounded_score)
