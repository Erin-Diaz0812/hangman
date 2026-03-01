#establishing foundation
import pandas as pd
import random
import csv
import os

def log_game_results(chosen_word, category, guesses_used, guess_count, won, guessed_letters):
    file_exists = os.path.exists('game_results.csv')
    
    with open('game_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['word', 'category', 'guesses_used', 'guesses_allowed', 'won', 'wrong_letters'])
        writer.writerow([chosen_word, category, guesses_used, guess_count, won, guessed_letters])


df = pd.read_csv('hangman_word_list.csv')

print("Welcome to my rendition of hangman!")

chosen_category = None
minimum_length = 3
maximum_length = 11
guess_count = 10
attempts_left = guess_count

#doing game set up
selection = input("Would you like to customize this game? (Yes or No) ")

if selection == "Yes":
    category_choice = input("Would you like to select a category? (Yes or No): ")
    if category_choice == "Yes":
        categories = ['animal', 'dessert', 'clothing', 'vehicles', 'foreign word']
        print("Categories: ", categories)
        chosen_category = input("Please select a category: ")

    length_choice = input("Would you like to set a word length range? (Yes or No) ")
    if length_choice == "Yes":
        minimum_length = int(input("What is the minimum word length you want (3 to 11)? "))
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
print(chosen_category) 
print(guess_count)

#actually turning this playable
display = []
for letter in chosen_word:
    display += '_'
print(display)

banned_letters = []
guessed_letters = []
play_again = True


while guess_count > 0 and '_' in display:
    guess_letter = input("Enter a letter to guess with: ").lower().strip()
    while not len(guess_letter) == 1:
        guess_letter = input("Can you enter a singular letter? ").lower()

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
        print("There are now: ", guess_count, "guesses remaining")
        print("Incorrect guessed letters are: ", *banned_letters)

    else:
        print("this letter is now banned")
        print(display)
        guess_count -=1
        print("There are now: ", guess_count, "guesses remaining")
        banned_letters.append(guess_letter)
        print("Banned (incorrect) letters are: ", *banned_letters)


guesses_used = attempts_left - guess_count
if '_' not in display:
    print("You guessed the correct word! ", chosen_word)
    log_game_results(chosen_word, chosen_category, guesses_used, guess_count, True, guessed_letters)
else:
    print("The word was: ", chosen_word)
    log_game_results(chosen_word, chosen_category, guesses_used, guess_count, False, guessed_letters)




'''
trying and failing to do a game loop. It broke too many things and took me about 2 hours before deciding that it won't be worth it.

        do_again = input("Would you like to play again? (Yes or No) ")
        if do_again != "Yes":
            break
        if do_again == play_again:
            continue

            

play_again = input("Would you like to play again? (Yes or No): ")
if play_again != "Yes":
    print("Thanks for playing!")
if play_again == "Yes":
    guess_count = 10
    display = []

    for letter in chosen_word:
        display += '_'
        print(display)
'''