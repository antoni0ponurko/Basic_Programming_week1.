word = input("Enter a word: ")
vowels = "aeiouAEIOU"
result = ""

for char in word:
    if char not in vowels:
        result += char


print(f"The string with the deleted vowels is: {result}")
