# Print all even numbers starting from 4 up till 100 one after another. Use a for-loop

s = ""

for i in range(11, 129, 2):
    s = s + str(i) + ", "
    s = s[: -2]

    print(s)
