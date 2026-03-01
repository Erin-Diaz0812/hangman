# hangman
HackUSU midterm project for two classes

For the graders, below is what each file does specifically.

round4.py = python terminal version of Hangman this is playable
index.html = website version (html, css, javascript) of Hangman - this is playable (click on settings > pages > visit site or use this link: https://erin-diaz0812.github.io/hangman/)
hangman_word_list.csv = the word list used in both round4.py and index.html

game_results.csv = when a game is completed in round4.py it's saved here
explode_game_results.py = splits up the wrong cell letter guess in game_results.csv to allow for data visualization and analysis
game_results_exploded.csv = the saved exploded result of explode_game_results.py
