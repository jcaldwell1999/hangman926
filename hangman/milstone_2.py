import random

word_list = [
    "Apples",
    "Grapes",
    "Oranges",
    "Blueberries",
    "Strawberries"
]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")
print("Good guess!" if len(guess) == 1 and guess.isalpha() else "Oops! That is nto a valid input.")