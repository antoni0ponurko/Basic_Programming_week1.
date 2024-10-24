def calculate(a, b, c=0, d=0):
    return a - b + c - d


result1 = calculate(10, 5, 3, 2)
result2 = calculate(a=10, b=5, c=3, d=2)
result3 = calculate(10, 5)


print(result1)
print(result2)
print(result3)
