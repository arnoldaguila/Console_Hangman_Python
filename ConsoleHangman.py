from random import randint


class Hangman:
    def __init__(self, txt_file):
        self.file = txt_file
        self.guesses_remaining = 6

    def get_word(self):
        # checking to see if you have a file.
        try:
            with open(self.file, "r") as word_file:
                word_bank = word_file.readlines()
                return word_bank[randint(0, len(word_bank) - 1)].strip()
        except FileNotFoundError:
            print("Please create or download a text file that has a list of words.")

    def print_hangman(self):
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


def main():
    file = "word_bank.txt"
    x = Hangman(file)
    print(x.get_word())


if __name__ == '__main__':
    main()
