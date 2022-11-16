from random import randint
def get_word(filename):
    '''
    This function gets and returns a random word from a text file that contains a lot of words.
    Version: November 16, 2022
    :param filename: word_bank.txt is a list of words.
    :return word_file_lines: String.
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
    :return: boolean
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
    :param number_of_guesses: Int
    :return: print()
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
    :param word: String
    :return:
    '''
    number_of_guesses = 6 # six parts of the body. Head, body, left arm, right arm, left leg, right leg.
    blank_lines = "_" * len(word)  # creating blank lines for user experience.
    blank_lines_list = list(blank_lines)
    guess_bank = [] # guess bank so that user can't input the same letter twice
    win = False  # creating a win/loss message
    loss = False

    while number_of_guesses != 0:
        print("Guesses Remaining: {}".format(number_of_guesses))
        print_hangman(number_of_guesses) # prints the gallow
        print("".join(blank_lines_list))
        user_input = input("Enter a letter: ") # userInput
        user_input = user_input.lower() # changing userInput to a lowercase letter.
        user_input = user_input.replace(" ", "") # getting rid of all spaces.
        print()
        if (len(user_input) > 1):
            if user_input == "end":
                print("Ending game.")
                return
            elif user_input == "restart":
                print("Restarting game.")
                console_game(word)
            else:
                print("Error: Invalid input.")
        else:
            if (ord(user_input) < 97) | (ord(user_input) > 122):
                print("Error: Invalid Input not a letter.")
            elif (user_input in guess_bank): # if letter has been guessed before.
                print("You guess the letter before dude!")
                print("".join(blank_lines_list))
            else:
                if(user_input not in word): # if letter is not in the word
                    guess_bank.append(user_input)
                    number_of_guesses = number_of_guesses - 1
                    # checking to see if number_of_guess is 0 for the loss message.
                    if number_of_guesses == 0:
                        loss = True
                        break
                else:
                    guess_bank.append(user_input)
                    for letter in user_input:
                        for i in range(len(word)):
                            if word[i] == letter:
                                blank_lines_list[i] = letter
                    if ("".join(blank_lines_list) == word):
                        win = True
                        print("".join(blank_lines_list))
                        break

    if loss:  # loss message
        print_hangman(number_of_guesses)
        print("You lost.")
        print("The word was {}".format(word))
        print()
        restart()

    if win: # win message
        print("You won!!")

def restart():
    '''
    This function is used to ask if the user wants to play again.
    :return:
    '''
    user_input = input("Do you want to play again? Enter Yes or No: ")
    user_input = user_input.lower()
    user_input = user_input.replace(" ", "")
    if user_input == "yes":
        print()
        print("Restarting game.")
        main()
    elif user_input == "no":
        print()
        print("Thank you for playing.")
        print("Ending game.")
        return
    else:
        print()
        print("Error: Invalid Input. Yes or No.")
        restart()

def main():
    '''
    This is the main function. It calls the game and get_word fucntion.
    :return:
    '''
    word = get_word("word_bank.txt")  # getting word
    console_game(word) # playing console hangman

if __name__ == '__main__': # script run.
    main()
