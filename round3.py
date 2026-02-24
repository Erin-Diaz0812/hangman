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
- display a list of banned letters
- create a way to add onto image
- have display look better when guessing letters
- 

'''

while guess_count >= 0 and '_' in display:
    guess_letter = input("Enter a letter to guess with: ").lower()

    good_guess = False
    for spot in range(len(chosen_word)):
        if chosen_word[spot] == guess_letter:
            display[spot] = guess_letter
            good_guess = True

    if good_guess:
        print("you guessed: ", guess_letter)
        print(display)
        guess_count -=1
        print(guess_count)
        print("There are now: ", guess_count, "guesses remaining")

    else:
        print("this letter is now banned")
        print(display)
        guess_count -=1
        print("There are now: ", guess_count, "guesses remaining")

if '_' not in display:
    print("You guessed the correct word! ", chosen_word)

else:
    print("The word was: ", chosen_word)

    #if guess is right then:
        #update display to show the letter
        #remove 1 from guess_count
        #