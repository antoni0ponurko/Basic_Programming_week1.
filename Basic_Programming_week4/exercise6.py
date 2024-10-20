# Ask the user for a word. Loop over the word. Store all the vowels together in one list, the consonants in
# another list. Print both lists. How do you make sure that both uppercase and lowercase letters end up in
# the correct list?

word = input(str("Enter you word :"))
consonants = []
vowels = []

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels.append(char)

else:
    consonants.append(char)

    print(f"The consonant are: {consonants}")
    print(f"The vowel are : {vowels}")
