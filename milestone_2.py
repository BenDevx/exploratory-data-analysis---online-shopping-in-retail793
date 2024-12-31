word_list = ["pineapple", "orange", "mango", "apple", "pear"]
print(word_list)

import random
word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
print(f"You entered: {guess}")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")