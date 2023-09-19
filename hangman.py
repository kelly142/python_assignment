import random
import string


'''
Group members: 
    -[x] Kagaba Shingiro Etienne
    -[x] Uwayo Anne Marie
    -[x] Uwayezu Alice
'''


def choose_random_word():
    word_list = ["hangman", "programming", "python", "openai", "challenge"]
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display


def hangman_game():
    word = choose_random_word()
    guessed_letters = []
    remaining_guesses = 6
    warnings = 3
    vowels = "aeiou"

    print("Welcome to Hangman!")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guesses remaining:", remaining_guesses)
        print("Letters not yet used:", "".join(set(string.ascii_lowercase) - set(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            if warnings > 0:
                warnings -= 1
                print("Please enter a valid letter. You have {} warnings left.".format(warnings))
            else:
                remaining_guesses -= 1
                print("Please enter a valid letter. You've run out of warnings. You lose a guess.")
        elif guess in guessed_letters:
            if warnings > 0:
                warnings -= 1
                print("You've already guessed that letter. You have {} warnings left.".format(warnings))
            else:
                remaining_guesses -= 1
                print("You've already guessed that letter. You lose a guess.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                print("Oops! That letter is not in the word.")
                if guess in vowels:
                    remaining_guesses -= 2
                else:
                    remaining_guesses -= 1

        if display_word(word, guessed_letters) == word:
            print("\nCongratulations! You've won! The word is:", word)
            score = remaining_guesses * len(set(word))
            print("Your score is:", score)
            break

        if remaining_guesses <= 0:
            print("\nSorry, you've run out of guesses. The word was:", word)
            break


if __name__ == "__main__":
    while(True):
        hangman_game()
        option = input("Do you want to play another game? Y or n (default Y): ")
        if option in "nN" and option != "":
            print(option, "hello")
            break
        else:
            continue

