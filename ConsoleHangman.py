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

        Args:
            user_input (str): The user input.

        Returns:
            None: None is used if user_input is END
            int: 1 is used if user_input is RESTART
            int: 2 is used if user_input not a letter or user_input has the length of greater than 1.
        """
        cleaned_input = user_input.replace(" ", "")
        cleaned_input = cleaned_input.upper()
        is_it_a_char = ord(cleaned_input)
        if cleaned_input == "END":
            return None
        elif cleaned_input == "RESTART":
            return 1
        elif len(cleaned_input) > 1:
            return 2
        elif is_it_a_char < 65 or is_it_a_char > 90:
            return 2
        elif len(cleaned_input) == 1:
            return cleaned_input

    def run(self):
        """
        Method that runs the game.
        """
        # Display game message.
        self.game_message()
        # Get a random word from the word bank file.
        the_word = self.get_word()
        # Game loop.
        while True:
            # Get user input.
            user_input = input()
            # Check user input is valid.
            cleaned_input = self.check_user_input(user_input)
            if cleaned_input is None:
                break
            elif cleaned_input == 1:
                restart = True
                break
            elif cleaned_input == 2:
                print("Error, invalid input.")
                print()
                continue
            elif isinstance(cleaned_input, str):
                if cleaned_input in the_word:
                    pass


def main():
    file = "word_bank.txt"
    x = Hangman(file)


if __name__ == '__main__':
    main()
