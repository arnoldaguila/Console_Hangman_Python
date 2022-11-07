from random import randint
def get_word(filename):
    '''
    This function gets and returns a random word from a text file that contains a lot of words.
    Version: November 6, 2022
    :param filename: word_bank.txt is a list of words.
    :return word_file_lines: String, random word from the word_bank.txt file.
    '''
    try: # checking to see if you have a file.
        with open(filename, "r") as word_file:
            word_file_lines = word_file.readlines()
            return word_file_lines[randint(0, len(word_file_lines) - 1)].strip()
    except FileNotFoundError:
        print("Please create or download a text file that has a list of words.")

def is_float(user_input):
    '''
    is_float()
    This function checks to see if the user input is a float.
    :param user_input: String, the param is a string that the user inputted
    :return: True | False: Boolean, returning true if user input is a float and a false otherwise.
    '''
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def print_hangman(number_of_guesses):
    '''
    print_hangman()
    This function returns a print statement, shaped as a gallow and stick figure.
    :param number_of_guesses: Int, the number of guesses the user has left.
    :return: print of gallow and stick figure.
    '''
    if number_of_guesses == 6:
        print("_________")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif number_of_guesses == 5:
        print("_________")
        print("|       |")
        print("|       O")
        print("|")
        print("|")
        print("|")
    elif number_of_guesses == 4:
        print("_________")
        print("|       |")
        print("|       O")
        print("|       |")
        print("|")
        print("|")
    elif number_of_guesses == 3:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      /|")
        print("|")
        print("|")
    elif number_of_guesses == 2:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|")
        print("|")
    elif number_of_guesses == 1:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|        \\")
        print("|")
    elif number_of_guesses == 0:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / \\")
        print("|")


def console_game(word):
    '''
    console_game()
    This function is the console game for hangman.
    Version: November 6, 2022
    :param word: String, a word that was pulled form get_word.
    :return:
    '''
    # six parts of the body. Head, body, left arm, right arm, left leg, right leg.
    number_of_guesses = 6
    # creating blank lines for user experience.
    blank_lines = "_" * len(word)
    blank_lines_list = list(blank_lines)
    # guess bank so that user can't input the same letter twice
    guess_bank = []
    # creating a win/loss message
    win = False
    loss = False

    while number_of_guesses != 0:
        print_hangman(number_of_guesses)
        print("".join(blank_lines_list))
        user_input = input("Enter a letter: ") # userInput
        user_input = user_input.lower() # if the userInput is a Capital letter.
        print()
        if user_input.isdigit() | is_float(user_input): # checking to see if user_input is an int or float.
            print("Invalid input, can't have integers or decimals as inputs, please input a letter.")
        elif len(user_input) > 1: # checking to see if the user_input has put more than 1 letter.
            print("Invalid input, please input 1 letter.")
        else:
            if (user_input in guess_bank): # if letter has been guessed before.
                print("You guess the letter before dude!")
                number_of_guesses = number_of_guesses - 1
                print("".join(blank_lines_list))
                print("Guesses Remaining: {} \n".format(number_of_guesses))
            else:
                # if letter is not in the word
                if(user_input not in word):
                    guess_bank = user_input
                    number_of_guesses = number_of_guesses - 1
                    # checking to see if number_of_guess is 0 for the loss message.
                    if number_of_guesses == 0:
                        loss = True
                        break
                    else:
                        print_hangman(number_of_guesses)
                        print("".join(blank_lines_list))
                        print("Guesses Remaining: {} \n".format(number_of_guesses))
                else:
                    guess_bank = user_input
                    for letter in user_input:
                        for i in range(len(word)):
                            if word[i] == letter:
                                blank_lines_list[i] = letter
                    if ("".join(blank_lines_list) == word):
                        win = True
                        print("".join(blank_lines_list))
                        break
                    else:
                        print("".join(blank_lines_list))
                        print("Guesses Remaining: {} \n".format(number_of_guesses))

    #loss message
    if loss:
        print_hangman(number_of_guesses)
        print("You lost.")
        print("The word was {}".format(word))

    #win message
    if win:
        print("You won!!")


# script run.
if __name__ == '__main__':
    word = get_word("word_bank.txt") # getting word
    print(console_game(word)) # playing console hangman
