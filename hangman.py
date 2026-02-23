#connect to a dictionary
import requests
import random

#function that will hold the word to guess
def word_to_guess(word):
    #list_words to return picked_word is me trying to see if I can get a word to be printed from a small list
    #list_words = ["apple", "food", "dog", "cat"]
    #picked_word = random.choice(list_words)
    #return picked_word

    #url down is me trying to connect to the dictionary api and print a random word
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/<word>"
    word_response = requests.get(url)
    chosen_word = random.choice(word_response)
    return chosen_word

print(word_to_guess("hello"))
