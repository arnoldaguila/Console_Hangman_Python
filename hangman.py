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
    number_of_guesses = 6 # six parts of the body. Head, body, left arm, right arm, left leg, right leg.
    blank_lines = "_" * len(word) # creating blank lines for user experience.
    blank_lines_list = list(blank_lines)
    while number_of_guesses != 0:
        guesses = []
        user_input = input("Enter a letter: ")
        guesses.append(user_input)
        for i in guesses:
            for j in range(len(word)):
                if word[j] == i:
                    blank_lines[j] = i
            return blank_lines





if __name__ == '__main__':
    word = get_word("word_bank.txt") # getting word
    print(word)
    print(console_game(word)) # playing console hangman
