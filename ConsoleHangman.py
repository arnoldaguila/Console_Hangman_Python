from random import randint


class Hangman:
    def __init__(self, txt_file):
        """
        Initializes the Hangman class.
        """
        self.file = txt_file

    @staticmethod
    def display(the_word, user_inputted_letter=None, target_index=None):
        """
        Creates underscores for display purposes.

        Returns:
            str: A string of underscores.
        """
        display = "_" * len(the_word)
        display_list = list(display)
        if user_inputted_letter is not None and target_index is not None:
            for i in range(len(the_word)):
                if (i == target_index) and (target_index is not None):
                    display_list[i] = user_inputted_letter
        return "".join(display_list)

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

    @staticmethod
    def print_hangman(guesses_remaining):
        """
        Displays the current state of the game.
        """
        if guesses_remaining == 6:
            print("_________")
            print("|       |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
        elif guesses_remaining == 5:
            print("_________")
            print("|       |")
            print("|       O")
            print("|")
            print("|")
            print("|")
        elif guesses_remaining == 4:
            print("_________")
            print("|       |")
            print("|       O")
            print("|       |")
            print("|")
            print("|")
        elif guesses_remaining == 3:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|")
            print("|")
            print("|")
        elif guesses_remaining == 2:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|\\")
            print("|")
            print("|")
        elif guesses_remaining == 1:
            print("_________")
            print("|       |")
            print("|       O")
            print("|      /|\\")
            print("|        \\")
            print("|")
        elif guesses_remaining == 0:
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

    def run(self):
        """
        Method that runs the game.
        """
        # Game loop so that user can restart.
        while True:
            # Get a random word from the word bank file.
            the_word = self.get_word()
            the_word_but_upper = the_word.upper()

            # Number of guesses remaining for the player.
            guesses_remaining = 6

            # Display game message.
            self.game_message()

            # Creating underscores for game display purposes. Exp. "_______"
            blank_lines = self.display(the_word)

            # Game loop.
            while True:
                self.print_hangman(guesses_remaining)
                print(blank_lines)
                print(f"The word: {the_word}")  # This is temp for testing purpose.

                # Get user input.
                user_input = input("Enter an letter: ")
                print()

                # Remove spaces from input, change the String to upper case, making sure the input is a char.
                cleaned_input = user_input.replace(" ", "")
                cleaned_input = cleaned_input.upper()
                char_len = ord(cleaned_input[0])
                # Getting the length to see if it is more than 1 letter.
                cleaned_input_length = len(cleaned_input)

                if cleaned_input == "END":
                    print("Ending game.")
                    print()
                    return
                elif cleaned_input == "RESTART":
                    print("Restarting Game.")
                    print()
                    break
                elif cleaned_input_length > 1:
                    print("Not 1 letter.")
                    print()
                elif cleaned_input_length < 1:
                    print("Enter a letter.")
                    print()
                elif char_len < 65 or char_len > 90:
                    print("Error: Not a letter.")
                    print()
                elif cleaned_input_length == 1:
                    if cleaned_input in the_word_but_upper:
                        location_of_letter = the_word_but_upper.index(cleaned_input)
                        blank_lines = self.display(the_word, location_of_letter)
                        print(blank_lines)
                    else:
                        guesses_remaining -= 1

                else:
                    print("Error: Invalid input.")
                    print()


def main():
    file = "word_bank.txt"
    x = Hangman(file)
    x.run()


if __name__ == '__main__':
    main()
