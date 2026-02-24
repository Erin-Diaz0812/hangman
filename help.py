import requests
import random

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1&length=5"
    response = requests.get(url)
    word_list = response.json()  # converts the response to a Python list
    return word_list[0]          # grabs the first (only) word from the list

chosen_word = get_random_word() 
print(chosen_word)


#displaying blanks for the word length
display = [] #creating a list that will have the "_"
for letter in chosen_word: #creating a for loop where for each letter selected under the function get_random_word; each character get's a blank line
    display += '_'
print(display) #prints the final amount of blank lines


guess_count = 10 #hard coding guess count, will need to make interactable later


for spot in range(len(chosen_word)):
    guess_letter = input("Can you enter a letter: ").lower() 
    letter = chosen_word[spot] #allows python to iterate through the word and input correct things
    print("Your guess:", guess_letter, "against: ", letter)
    if letter == guess_letter: #letter in chosen_word:
        display[spot] = letter
        print(display)
        #correct will swap out blanks for the letter and save them/update the list
        #ignore: update the guess counter

    else: 
        print("this letter is now banned! ")
        #if letter guess was wrong
        #deincrement the amount of guesses allowed
        # post the wrong letter somewhere for reference in the future
        #add onto stick man.
        #maybe figure out a way to prevent the user from inputting the letter again?