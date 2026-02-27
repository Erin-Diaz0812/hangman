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



2/26
made more progress on set up logic, but I think I've confused myself somewhere. It feels very muddled together and I don't know if that many if statements are a good move, a bad move, if some should be swapped to elifs or if it should be scrapped.

I just did my first run through and I think the logic is logicing correctly! I forgot that the word is still being picked at random, so you can guess why I was so confused when I selected animal and had to guess "typhoon" instead. lol but honestly though, this is probably the first moment where it actually felt like a lot of fun to play!

Ended up scrapping my initial idea for selection criteria because I saw something else that made a bit more sense and was easier to read lowkey, my version also was limiting to one adjustment rather than allowing for multiples. 

When I ran the updated selection statement, when you filter by category you run into an error, that's related to the filtering dataframe for categories. So I did a bit of looking around and I think that .iloc[] is the answer. However, it doesn't allow for random selection easily, it needs extra code which I don't understand there is also a .loc[] floating around too but I also don't understand that.
Option 1: https://stackoverflow.com/questions/74641988/pandas-keyerror-in-get-loc-when-calling-entries-from-dataframe-in-for-loop
option 2: https://stackoverflow.com/questions/15923826/random-row-selection-in-pandas-dataframe
( File "/usr/local/python/3.12.1/lib/python3.12/site-packages/pandas/core/frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3648, in get_loc
    raise KeyError(key) from err)


Line 45 has the potential solution. Basically it'll tell me what python is actually reading all the column headers as rather than is printed off in the data frame. Which was the solution! Basically in my initial category sort and the DF I had 'categories' which worked and was printed in both areas but python was actually reading it as 'main-category'. Swapped it around and it worked! 

all links open on home mac:
https://stackoverflow.com/questions/74641988/pandas-keyerror-in-get-loc-when-calling-entries-from-dataframe-in-for-loop
https://stackoverflow.com/questions/15923826/random-row-selection-in-pandas-dataframe
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
https://www.geeksforgeeks.org/python/exporting-variable-to-csv-file-in-python/
2 searches:
1. what is iloc in python pandas
2. how to do a random selection within .iloc[]


To-do:
- move variables around (remember python will read and accept the latest/last variable that has a result associated with it. Chosen word is before the selection menu, but they aren't able to provide a word at the moment = initial all random chosen word is used. AND guess_count the hard coded 10 is after the selection so it's going with hard code no matter what)
- figure out how to print the category if it was chosen or is randomly selected
- prevent multiple letter guesses!!! (I accidentally did one where I did "ei" as a guess and it was accepted)

I think that this might be a good spot to pause, since the next step is making the live csv file (which should probably be done on laptop for Tableau) and then we go into website, image increments, and data viz side of this project. i think by now, this project is around 11 hours worth of work. 
(most of which it feels like Claude ended up coding for me but I tried! I looked around for references as to how things could work, tried to debug, and more. Mainly Claude was used as a way to help me keep moving, debugging, or if I was stuck somewhere. Although, I was debugging everywhere and was stuck everywhere so it feels like Claude coded everything for me. The main thing I brought in and is fully human is the idea, structure, the wordle-style flow, word list, category logic, customization, etc. Claude claims to have mainly helped with syntax and explaining why things weren't working but it feels like Claude did a lot more than that. :( )


2/27:
okay, game and live update csv file is basically done! So onto website now.
What happened to complete the game is trying to do a python loop (and failing at it, so this is now a website issue) and then finalizing the export csv file feature, ensuring that this csv file is being live updated.

