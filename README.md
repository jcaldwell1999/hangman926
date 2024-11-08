# Hangman

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation Instructions

1. Clone the repository by entering "https://github.com/jcaldwell1999/hangman926.git" into your terminal in your desired directory.

## Usage Instructions

### Milestone 3 

1. Ensure working directory is "hangmnan926/hangman/milestone_3".
1. In bash / terminal, enter "python milestone_3.py".
1. Respond to prompt by entering a letter.
1. Game will check if the letter guessed is valid, and will ask to re-enter if not.
1. Game will check if the letter is in the randomly chosen item from the list, and announce to user if correct or not.

### Milestone 4

1. Ensure your working directory is set to "hangman926/hangman?".
1. In your bash / terminal, enter "python milestone_4.py".
1. The game will prompt you to guess a letter.
1. The game will validate the input:
    - If the input is invalid (not a single alphabetical letter), you will be prompted to re-enter.
    - If the letter has already been guessed, it will notify you.
1. If the guess is correct, the letter will be revealed in the word. If it's incorrect, you will lose a life, with remaining lives displayed.
1. Continue guessing until you guess the word correctly, or run out of lives.


## File Structure

- **hangman926:** Root directory of project
- **hangman:** Directory holding Python files
    - `milestone_3.py`: Basic letter validation and guessing functionality
    - `milestone_4.py`: Class-based Hangman with lives, guess tracking, and input validation.

## License Information