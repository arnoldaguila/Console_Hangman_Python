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
    # creating a win/loss message
    win = False
    loss = False
    while number_of_guesses != 0:
        user_input = input("Enter a letter: ") # userInput
        if len(user_input) > 1:
            print("Invalid input, please input 1 letter.")
        else:
            # if letter is not in the word
            if((user_input in word) == False):
                number_of_guesses = number_of_guesses - 1
                if number_of_guesses == 0:
                    loss = True
                    break
                else:
                    print("".join(blank_lines_list))
                    print("Guesses Remaining: {} \n".format(number_of_guesses))
            else:
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

    if win:
        print("You won!!")


# main method
if __name__ == '__main__':
    word = get_word("word_bank.txt") # getting word
    print(word)
    print(console_game(word)) # playing console hangman
