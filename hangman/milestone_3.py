import random

# Fruit list
fruit_list = [
    "Apples",
    "Grapes",
    "Oranges",
    "Blueberries",
    "Strawberries"
]

# Choose random fruit
random_fruit = random.choice(fruit_list)

# Infinite loop
'''
while True:
    # Get user letter input
    guess = input("Enter a single letter: ")

    # Check input is a single letter
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in random_fruit.lower():
            print("Good guess! " + guess + " is in the word.")
            break
        else:
            print("Sorry, " + guess + " is not in the word. Try again.")
    else:
        print("Invalid letter. Please enter a single alphabetical character.")
'''

def check_guess(guess):
    guess = guess.lower()
    if guess in random_fruit.lower():
        print("Good guess! " + guess + " is in the word.")
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")

def ask_for_input():
    
    while True:
        guess = input("Enter a single letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid Letter. Pease enter a single alphabetical character.")

ask_for_input()