word = input("Enter a word:> ")

vowels_list = []
consonants_list = []

vowels = "aeiou"

for letter in word:
    lower_letter = letter.lower()

    if lower_letter in vowels:
        vowels_list.append(letter)

    elif lower_letter.isalpha():
        consonants_list.append(letter)

print("The vowels are:", vowels_list)
print("The consonants are:", consonants_list)
