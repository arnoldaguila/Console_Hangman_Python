# Console_Hangman_Python
My take on a python hangman console game. Alot of bugs and features missing that I added in the java version of the game. (Work in progress)


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
Probably need to implement an ASCII conditional.

Version November 8, 2022

- Found bug, if user inputs the same letter till the number of runs 0 no loss message will occur
and the hangman print won't finish.
- Fount an error with the guess_bank. the user input was not appending to the guess bank.
