n1 = int(input("Give the first number: "))
n2 = int(input("Give a different number: "))
n3 = int(input("Give another differen number:"))


def show_max(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(show_max(n1, n2, n3))
print(show_max(1, 2, 3))
print(show_max(2, 3, 1))
print(show_max(3, 2, 1))
