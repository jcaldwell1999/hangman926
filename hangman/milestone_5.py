# Milstone 5

# Imports
import random

# Hangman Class
class Hangman():

    def __init__(self, word_list, num_lives=5):
        """
        Intialises the Hangman game witha  list of words and a number of lives.
        A random word is chosen, and is setup for the game.

        Parameters:
        word_list: A list of possible words for the game.
        num_lives: The current number of lives the user has. Default is 5.
        word: The randomly chosen word.
        word_guessed: Initially a hidden word depicted by "_" for each letter. With each correct guess, the letter is revealed.
        num_letters: The number of letters in the randomly chosen word.
        list_of_guesses: A list storing all previous guesses made by the user.
        """
        # Attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        """Updates teh word_guessed list with the guessed letter"""
        for index, letter in enumerate(self.word.lower()):
                if guess == letter:
                    self.word_guessed[index] = guess # Replaces underscore with correct letter

    def check_guess(self, guess):
        """
        Processes a guessed letter. Checks if it's in teh word, and updates the game.

        Parameters:
        guess: The letter guesses by the player.
        """
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
            # Decrement num_letters if guess was a new letter
            self.num_letters -= 1
        else:
            self._decrement_lives(guess)

    def _decrement_lives(self, guess):
        """Reduces lives by one and prints an update"""
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")


    # Method to ask for, and validate, user's input
    def ask_for_input(self):
        """Prompts user for input, validates it, and processes the guess."""
        # Input validation loop
        while True:
            guess = input("Enter your guess: ").lower()
            if self._validate_guess(guess):
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def _validate_guess(self, guess):
        """ Checks if the guess is valid and hasn't been used."""
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
            return False
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True
    
    def play_game(self, word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print("You Lost")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations! You wont the game!")
                break


word_list = ["Apples", "Mangos", "Grapes", "Oranges"]

game_test = Hangman(word_list)

game_test.play_game(word_list)
                
