from random import randint

def get_word(filename):
    '''
    This function gets and returns a random word from a text file that contain a lot of words.
    :param filename: word_bank.txt is a list of words.
    :return: random word from the word_bank.txt file.
    '''
    with open(filename, "r") as word_file:
        word_file_lines = word_file.readlines()
        return word_file_lines[randint(0, len(word_file_lines) - 1)].strip()

def console_game(word):
    guesses = []
    number_of_guesses = 6 # six parts of the body. Head, body, left arm, right arm, left leg, right leg.
    user_guess = input("Enter a letter: ")




if __name__ == '__main__':
    print(get_word("word_bank.txt"))