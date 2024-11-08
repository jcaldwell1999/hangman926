import random

# Fruit list
possible_fruits = [
    "Apples",
    "Grapes",
    "Oranges",
    "Blueberries",
    "Strawberries"
]

# Choose random fruit
secret_word = random.choice(possible_fruits)

# Old Code
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

# Checks guess 
def check_letter_in_word(guess, word):
    guess = guess.lower()
    if guess in word.lower():
        print("Good guess! " + guess + " is in the word.")
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")

def ask_for_input():
    
    while True:
        guess = input("Enter a single letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            check_letter_in_word(guess, secret_word)
            break
        else:
            print("Invalid Letter. Pease enter a single alphabetical character.")

ask_for_input()