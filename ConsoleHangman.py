from random import randint


class Hangman:
    def __init__(self, txt_file):
        """
        Initializes the Hangman class.
        """
        self.file = txt_file
        self.guesses_remaining = 6

    def get_word(self):
        """
        Chooses and returns a random word from the instance file.

        Returns:
            str: A random word from file.
        """
        # checking to see if you have a file.
        try:
            with open(self.file, "r") as word_file:
                word_bank = word_file.readlines()
                return word_bank[randint(0, len(word_bank) - 1)].strip()
        except FileNotFoundError:
            print("Please create or download a text file that has a list of words.")
            return None

    def print_hangman(self):
        """
        Displays the current state of the game.
        """
        if self.guesses_remaining == 6:
            print("_________")
            print("|       |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
        elif self.guesses_remaining == 5:
            print("_________")
            print("|       |")
            print("|       O")
            print("|")
            print("|")
            print("|")
        elif self.guesses_remaining == 4:
            print("_________")
            print("|       |")
            print("|       O")
            print("|       |")
            print("|")
            print("|")
        elif self.guesses_remaining == 3:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|")
            print("|")
            print("|")
        elif self.guesses_remaining == 2:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|\\")
            print("|")
            print("|")
        elif self.guesses_remaining == 1:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|\\")
            print("|        \\")
            print("|")
        elif self.guesses_remaining == 0:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|\\")
            print("|      / \\")
            print("|")

    @staticmethod
    def game_message():
        """
        Print out a welcome and controls message. The control message will inform the user of the game features.
        """
        print()
        print("Hello, Welcome to Arnold's console hangman game.")
        print("You can end the game at anytime by typing in 'end', when asked to input a letter.")
        print("You can also restart at anytime by typing in restart.")

    def check_user_input(self, user_input):
        """
        Checks and cleans the argument by removing all spaces and setting the str to upper. This method also checks
        if the argument is valid i.e. the argument is a 1 letter.

        Parameters:
            user_input (str): The user input.
        """
        cleaned_input = user_input.replace(" ", "")
        cleaned_input = cleaned_input.upper()
        if cleaned_input is "END":
            pass
        elif cleaned_input is "RESTART":
            pass
        elif len(cleaned_input) > 1:
            pass

    def run(self):

        self.game_message()
        while True:
            user_input = input()


def main():
    file = "word_bank.txt"
    x = Hangman(file)


if __name__ == '__main__':
    main()
