# hangman
HackUSU midterm project for two classes

Currently doing most work in help.py but will need to swap over to hangman.py because help has a random word generator which prevents a lot of flexibility in the future (difficulty in terms of word being common, show definition at the end of game, category).


2/24:
created 3 iterations of the hangman base game loop

2/25:
fixing guess counter (would go to -1 before ending the loop, swap from >= to > and it was fixed)
create a "ban" variable of incorrect letters guessed 
(Need to decide if want to append first then print or print then append. Basically do I want the list to show the most recent guessed---like it was literally just typed in--- or do I want the most recent guess be the one in the previous turn. Another way to think about this is: Do I want the letter A to show up in banned list turn 1 or the banned list on turn 2?)


To - Do:
- decide on banned letter append and print statement sequencing - line 13 in (has the note) - DONE! My brain liked it more when the append was before the print statement
- store letters and prevent the user from guessing it again - DONE!
- ensure all letters are an alpha > .isalpha() - DONE!

