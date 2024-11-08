# Milstone 4

# Imports
import random

# Hangman Class

class Hangman():

    def __init__(self, word_list, num_lives=5):
        # Attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            # Loop through each letter with its index
            for index, letter in enumerate(self.word.lower()):
                if guess == letter:
                    self.word_guessed[index] = guess # Replaces underscore with correct letter
            # Decrement num_letters if guess was a new letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    # Method to ask for, and validate, user's input
    def ask_for_input(self):

        # Input validation loop
        while True:
            #Guess Input
            guess = input("Enter your guess: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Pease enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

word_list = ["Apples", "Mangos", "Grapes", "Oranges"]

game = Hangman(word_list)

game.ask_for_input()
                
