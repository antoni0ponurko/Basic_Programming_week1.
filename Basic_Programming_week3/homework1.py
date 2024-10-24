word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in word:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
