word1 = input("Pleas enter a word: ")
word2 = input("Please enter a word: ")


def swap(s1: str, s2: str,) -> str:
    s = s1[:2]+s2[2:] + " " + s[:2] + s1[2:]
    return s


print(swap(word1, word2))
