# hangman
HackUSU midterm project for two classes

Currently doing most work in help.py but will need to swap over to hangman.py because help has a random word generator which prevents a lot of flexibility in the future (difficulty in terms of word being common, show definition at the end of game, category).


2/24:
created 3 iterations of the hangman base game loop (hangman > help > round3)

2/25:
fixing guess counter (would go to -1 before ending the loop, swap from >= to > and it was fixed)
create a "ban" variable of incorrect letters guessed 
(Need to decide if want to append first then print or print then append. Basically do I want the list to show the most recent guessed---like it was literally just typed in--- or do I want the most recent guess be the one in the previous turn. Another way to think about this is: Do I want the letter A to show up in banned list turn 1 or the banned list on turn 2?)

after a bit of chatting with Claude the next thing that'll happen is making the word list. This will be done in excel, exported as a .csv file with three columns: word, category, length (letters). Yes, there will only be one category, it won't be the end of the world. So I guess I'll stop here, and tomorrow either finish up the word list or create a new python file and import the csv word list!


To - Do:
- decide on banned letter append and print statement sequencing - line 13 in (has the note) - DONE! My brain liked it more when the append was before the print statement
- store letters and prevent the user from guessing it again - DONE!
- ensure all letters are an alpha > .isalpha() - DONE!


Next steps:
- swap from random word generator to a word source file (allows for difficulty, categories, word length, randomization, etc.)
- create the category and difficulty selection logic in python
- hangman image increments
- incorrect letter display
- website (buttons to click through, the screens, etc.)

- towards the end: viz and stats logging


2/25:
- upload the csv word list to github and be confused as to why it's not showing up in the pane on the left
- make round 4 file (basically copying round 3 but instead of random words it'll pull from the csv file)
- it's been 30 minutes of hitting nothing but barriers. Firstly the csv file didn't exist fully, then I couldn't get it to be read, then the random function wouldn't work. So lines 1-7 (import pands to print(chosen_word) are all Claude's writings
- then it's really jsut copying and pasting round 3 over to round 4

Now the next big monumental thing to deal with is game set up function.
I need this to be a function that's capable of allowing someone to choose which category, a word length or if they want a completely random word. 

I got to creating a if statement for categories. 