# Hangman_console_game
My take on a python hangman game.


Version November 1, 2022

- Found a bug with the user not getting a stike to the number_of_guess, if the user inputs the correct letter twice.
- Fixed the user not getting a strike for inputing the same letter twice.
- Need to create an actual Hangman now with tkinter.

Version November 6, 2022

- Check to see if the user is inputting an int or a float.
- Trying to figure out how to use tkinter.
- Found that inputting a decimal gives out the same message as inputting multiple letters.
- Created versions in the doc comments.
- Implementing a try except in the get_word function.
- Created an is_float function to check if the user input is a float.
- Found a bug. If user inputs a symbol like ';' or ']' program will accept the input.