#establishing foundation
import pandas as pd
import random

df = pd.read_csv('hangman_word_list.csv')

print(df)

#just me seeing if the base loop works. This is randomly selecting from the ENTIRE list
# chosen_word = df['word'].sample(1).values[0] #df['word'] = grab word column; sample(1) = pick a random row; value[0] = extraction to plain string
#print(chosen_word)

print("Welcome to my rendition of hangman!")

'''
initial filtering idea:
#allow for game customization: categories, word length, randomization, guess counter
selection = input("Would you like to choose the category, word length, or amount of guesses you'll have during this session? Please enter Yes or No: ")

if selection == 'Yes':
    selection2 = input("Which of the options would you like to pick from? \nCategories \n Word length \n Guess count")
    
    if selection2 == "Categories":
        categories = ['animal', 'dessert', 'clothing', 'vehicles', 'foreign word']
        print("Categories: ", categories)
        chosen_category = input("Please select a category: ")

    if selection2 == "Word length":
        minimum_length = int(input("What is the minimum word length you want (3 to 11)? "))
        maximum_length = int(input("What isi the maximum word length you want (3 to 11)? "))
        
    if selection2 == "Guess count":
        guess_count = int(input("How many guesses would you like (recommend between 6 to 10)? "))

else:
    chosen_word = df['word'].sample(1).values[0] #df['word'] = grab word column; sample(1) = pick a random row; value[0] = extraction to plain string
    print(chosen_word)
'''

chosen_category = None
minimum_length = 3
maximum_length = 11
guess_count = 10

#print(df.columns.tolist()) GenAI suggestion to see what python/csv is reading the column headers

selection = input("Would you like to customize this game? (Yes or No)")

if selection == "Yes":
    category_choice = input("Would you like to select a category? (Yes or No): ")
    if category_choice == "Yes":
        categories = ['animal', 'dessert', 'clothing', 'vehicles', 'foreign word']
        print("Categories: ", categories)
        chosen_category = input("Please select a category: ")

    length_choice = input("Would you like to set a word length range? (Yes or No)")
    if length_choice == "Yes":
        inimum_length = int(input("What is the minimum word length you want (3 to 11)? "))
        maximum_length = int(input("What is the maximum word length you want (3 to 11)? "))

    guess_choice = input("Would you like to set your guess count? (Yes or No): ")
    if guess_choice == "Yes":
        guess_count = int(input("How many guesses would you like (recommend between 6 to 10)? "))

filtered_df = df[(df['length'] >= minimum_length) & (df['length'] <= maximum_length)]

if chosen_category:
    filtered_df = filtered_df[
        (filtered_df['main category'] == chosen_category) |
        (filtered_df['sub-category'] == chosen_category)
    ]


chosen_word = filtered_df['word'].sample(1).values[0]
print(chosen_category) #figure out a way to print out category if they reject customizing the game; this will have to be a DF thing
print(guess_count)
print(chosen_word) #will need to comment out

#actually turning this playable
display = []
for letter in chosen_word:
    display += '_'
print(display)

#guess_count = 10 #swap to optional input later

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




#inaccurate way to do this now
#chosen_word = random.hangman_word_list.csv
#print(chosen_word)