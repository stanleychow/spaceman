import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    correct_counter = 0
    for letter in secret_word:
        if letter in letters_guessed:
            correct_counter += 1
            if correct_counter == len(secret_word):
                return True
    return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    display = ""
    for guess in secret_word:
        if guess in letters_guessed:
            display += guess
        else:
            display += "-"

    return display
    # pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    return guess in secret_word




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    play_game = True
    attempts = 7
    letters_guessed = [] # has to be unique; use a dictionary

    #TODO: show the player information about the game according to the project spec
    print("Spaceman is a guessing game. Guess the word before you run out of guesses!") # check this
    print(get_guessed_word(secret_word, letters_guessed)) # check this

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    print("Guess one letter per round!")
    attempts = 7
    # guessed_letter = input()  # weird to me

    while play_game and is_word_guessed(secret_word,letters_guessed) == False and attempts > 0:
        guess = input("Guess a letter: ")
        guess.lower()

        if len(guess) != 1: # letter guessed has to be 1
            print("Please only guess one letter.")

        if guess in secret_word: # has to be a single char that is in the secret_word

            if guess in letters_guessed:
                print("You already guessed that. Please guess again.")


            else:
                letters_guessed.append(guess)
                print('Correct!' + get_guessed_word(secret_word, letters_guessed))
        else:
            if len(guess) != 1:
                print("Please only guess one letter.")
            if guess in letters_guessed:
                print("You already guessed that. Please guess again.")
            else:
                letters_guessed.append(guess)
                attempts -= 1
                print('Incorrect!' + get_guessed_word(secret_word, letters_guessed))
                print("You have {} guesses left.".format(attempts))





    if is_word_guessed(secret_word, letters_guessed):
        print("You've won the game! You guessed the word " + secret_word)
        answer = input("Do you want to play again?")
        if answer in ('yes', 'y'):
            play_game = True
            spaceman(load_word())
        else:
            play_game = False
            print("Thanks for playing!")
    else:
        print("You've lost the game! The correct word was " + secret_word)
        answer = input("Do you want to play again?")
        if answer in ('yes', 'y'):
            play_game = True
            spaceman(load_word())
        else:
            play_game = False
            print("Thanks for playing!")





#These function calls that will start the game
secret_word = load_word()
#spaceman(secret_word)

#Unit Tests
def test_1():
    assert get_guessed_word("tiger", ["t", "y", "h"]) == "t----"

test_1()

def test_2():
    assert is_guess_in_word("t", "tiger") == True

test_2()

def test_3():
    assert is_word_guessed("tiger", ["t", "i", "g"]) == False

test_3()
