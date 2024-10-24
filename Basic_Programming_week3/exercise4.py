s = ""

for i in range(11, 129, 2):
    s = s + str(i) + ", "
    s = s[: -2]

    print(s)
