
'''
foundation to do list:
- update the api to be a dictionary
- set up categories, word length options, and difficulty
'''
import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1&length=5"
    response = requests.get(url)
    word_list = response.json()  # converts the response to a Python list
    return word_list[0]          # grabs the first (only) word from the list

chosen_word = get_random_word() 
print(chosen_word)

display = [] 
for letter in chosen_word: 
    display += '_'
print(display)

guess_count = 10 #can swap to input later on

'''
while loop to do list
- display a list of banned letters - done!
- create a way to add onto image
- have display look better when guessing letters - done!
- track guessed letters to prevent guessing them again - done!


'''
banned_letters = []
guessed_letters = []

while guess_count > 0 and '_' in display:
    guess_letter = input("Enter a letter to guess with: ").lower()

    while not guess_letter.isalpha():
        guess_letter = input("Re-enter a viable English letter: ").lower()

    if guess_letter in guessed_letters:
        print("Unfortunately, you've already guessed that letter.")
        continue

    guessed_letters.append(guess_letter)

    good_guess = False
    for spot in range(len(chosen_word)):
        if chosen_word[spot] == guess_letter:
            display[spot] = guess_letter
            good_guess = True

    if good_guess:
        print("you guessed: ", guess_letter)
        print(display)
        guess_count -=1
        print("There are now: ", guess_count, "guesses remaining")
        print("Incorrect guessed letters are: ", *banned_letters)

    else:
        print("this letter is now banned")
        print(display)
        guess_count -=1
        print("There are now: ", guess_count, "guesses remaining")
        banned_letters.append(guess_letter)
        print("Banned (incorrect) letters are: ", *banned_letters)


if '_' not in display:
    print("You guessed the correct word! ", chosen_word)

else:
    print("The word was: ", chosen_word)

