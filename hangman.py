from random import randint

def get_word(filename):
    '''
    This function gets and returns a random word from a word bank.
    :param filename: word_bank.txt is a list of words.
    :return: random word from the word_bank.txt file.
    '''
    word_file = open(filename, 'r')
    word_file_readline = word_file.readline()
    return word_file_readline[randint(0, len(word_file_readline) - 1)].strip()

def console_game(word):
    guesses = []



if __name__ == '__main__':
    pass