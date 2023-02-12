# This program checks whether a given string is a pangram and if it is not,
# the program also prints the missing letters.

# A pangram is a sentence which contains every letter form the english alphabets.

sentence = input("Enter a sentence to check: ").lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"
missing = []


for item in alphabets:
    if item not in sentence:
        missing.append(item)
    
if len(missing) == 0:
    print("Is a pangram")
else: 
    print("Is not a pangram")
    print(missing)
