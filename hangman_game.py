import random

def select_random_word():
    # List of words for the game
    word_list = [ 'pineapple', 'mango', 'strawberry', 'apple', 'banana', 'orange', 'grape','blueberry', 
                 'watermelon', 'cherry' , 'apricot' , 'kiwi' , 'papaya' , 'pomegranate' , 'plum' , 
                 'fig' , 'pear' , 'guava' , 'avocado' , 'peach']
    # Randomly select a word from the list
    return random.choice(word_list)

def display_word_state(word, guessed_letters):
    # Display the current state of the word with guessed letters
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {display}")

def play_hangman():
    print("Welcome to Hangman Game!")
    word_to_guess = select_random_word()
    guessed_letters = []
    attempts = len(word_to_guess) + 2  # Length of the word + 2 chances
    correct_guesses = 0

    while attempts > 0:
        display_word_state(word_to_guess, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            correct_guesses += word_to_guess.count(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word. You have {attempts} attempts left.")

        if correct_guesses == len(word_to_guess):
            print(f"Congratulations! You've guessed the word '{word_to_guess}' correctly.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    play_hangman()
