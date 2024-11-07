import random

fruit_list = [
    "Apples",
    "Grapes",
    "Oranges",
    "Blueberries",
    "Strawberries"
]

print(fruit_list)

random_fruit = random.choice(fruit_list)

print(random_fruit)

letter_input = input("Enter a single letter: ")
print("Good guess!" if len(letter_input) == 1 and letter_input.isalpha() else "Oops! That is nto a valid input.")