from random import randint

def get_word(filename):
    '''
    This function gets and returns a random word from a text file that contain a lot of words.
    :param filename: word_bank.txt is a list of words.
    :return word_file_lines: String, random word from the word_bank.txt file.
    '''
    with open(filename, "r") as word_file:
        word_file_lines = word_file.readlines()
        return word_file_lines[randint(0, len(word_file_lines) - 1)].strip()

def console_game(word):
    '''
    This function is the console game for hangman.
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
        print("".join(blank_lines_list))
        user_input = input("Enter a letter: ") # userInput
        print()
        if len(user_input) > 1:
            print("Invalid input, please input 1 letter.")
        else:
            # if letter has been guessed before.
            if ((user_input in guess_bank) == True):
                print("You guess the letter before dude!")
                number_of_guesses = number_of_guesses - 1
                print("".join(blank_lines_list))
                print("Guesses Remaining: {} \n".format(number_of_guesses))
            else:
                # if letter is not in the word
                if((user_input in word) == False):
                    guess_bank = user_input
                    number_of_guesses = number_of_guesses - 1
                    # checking to see if number_of_guess is 0 for the loss message.
                    if number_of_guesses == 0:
                        loss = True
                        break
                    else:
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
        print("You lost.")
        print("The word was {}".format(word))

    #win message
    if win:
        print("You won!!")


# main function?
if __name__ == '__main__':
    word = get_word("word_bank.txt") # getting word
    print(console_game(word)) # playing console hangman
