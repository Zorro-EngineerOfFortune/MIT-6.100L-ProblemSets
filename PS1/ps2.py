# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------
# Define the file name where the list of words is stored
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # Open the word list file in read mode ('r')
    inFile = open(WORDLIST_FILENAME, "r")
    # Read the single line containing all words
    line = inFile.readline()
    # Split the line into a list of individual words
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    # Use random.choice to select one word uniformly at random
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Convert the secret word string to a list of characters
    secret_word_list = list(secret_word)
    # Initialize a counter to track letters correctly guessed
    counter = 0
    # Loop through every unique letter in the secret word
    for i in secret_word_list:
        # Check if the letter 'i' is present in the list of guessed letters
        if i in letters_guessed:
            # If present, increment the counter
            counter += 1
    # Check if the number of correctly guessed letters equals the total length of the word
    if counter == len(secret_word_list):
        # If they match, the player has won
        success = True
    else:
        # Otherwise, the player has not yet won
        success = False
    return success


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Convert the secret word string to a list of characters
    secret_word_list = list(secret_word)
    # Initialize the string that will show the progress (e.g., c*t)
    word_progress = ""
    # Initialize a counter to check if the *most recent* guess was correct
    good_guess = 0

    # Loop 1: Build the partially guessed word string
    for i in secret_word_list:
        # Check if the letter 'i' has been guessed
        if i in letters_guessed:
            # If yes, reveal the letter
            word_progress += i
        else:
            # If no, show an asterisk
            word_progress += "*"
    # Loop 2: Check the result of the *last* guess and print feedback
    for i in secret_word_list:
        # Check if the current letter of the secret word matches the very last letter guessed
        if i == letters_guessed[len(letters_guessed) - 1]:
            # If the last guess was a hit, increment good_guess counter
            good_guess += 1
        else:
            word_progress += "*"
    # Print guess feedback (Good/Oops).
    if good_guess > 0:
        print("Good guess!")
    else:
        print("Oops, that letter is not my my secret word :(")
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Define the full alphabet string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Convert alphabet to a list (less necessary but follows existing style)
    alphabet_list = list(alphabet)
    # Initialize the string for available guesses
    available_guesses = ""
    # Loop through every letter in the alphabet
    for i in alphabet_list:
        # Check if the letter 'i' has NOT been guessed
        if i not in letters_guessed:
            # If not guessed, append it to the available string
            available_guesses += i
    return available_guesses


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = choose_word(wordlist)
    # Initialize the number of guesses remaining
    number_guesses = 10
    win = 0
    # Initialize the list/string of letters guessed (currently a string)
    letters_guessed = ""
    # Define the vowels for scoring (used later, but currently not used correctly)
    vowels = "aeiou"
    # Initial game introduction and secret word length announcement
    print(
        "Welcome to Hangman!\nI am thinking of a word that is",
        len(secret_word),
        "letters long.",
    )
    # Show the initial set of available letters
    print("Available letters: ", get_available_letters(letters_guessed))
    # Use a for loop to iterate over the maximum number of guesses (10)
    for i in range(number_guesses):
        # Use a nested while loop to control game flow within each round
        while win == 0 and number_guesses != 0:
            print("_____________")
            print("You have", number_guesses, "guesses left")
            # Prompt user for a guess and append it to the letters_guessed string
            letters_guessed = letters_guessed + input("Please guess a letter: ")
            # Print the word progress (this function also incorrectly prints feedback)
            print(get_word_progress(secret_word, letters_guessed))
            # Print the remaining available letters
            print(get_available_letters(letters_guessed))
            # Deduct ONE guess after every guess
            number_guesses = number_guesses - 1
            # Check for win condition
            if has_player_won(secret_word, letters_guessed) == True:
                win = 1
                print("Congratulations! You WON")
            else:
                win = 0
        break
    # Print game-over message if the loop finished (either due to running out of guesses or the premature break)
    return print("Sorry, you ran out of guesses. The word was - ", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test


# To test your game, uncomment the following three lines.

# secret_word = choose_word(wordlist)
# hangman(secret_word)

# After you complete with_help functionality, change with_help to True
# and try entering "!" as a guess!

###############

# SUBMISSION INSTRUCTIONS
# -----------------------
# It doesn't matter if the lines above are commented in or not
# when you submit your pset. However, please run ps2_student_tester.py
# one more time before submitting to make sure all the tests pass.
