import random

magic_number = random.randint(1,999)
guesses = 5
while guesses > 0:
    guess_string = ""
    while not guess_string.isdigit():
        guess_string = input(f"Guess an integer between 0 and 1000, you have {guesses} guesses left:")
    guess = int(guess_string)
    if guess == magic_number:
        print("Correct, well done!")
        break
    elif guesses == 1:
        print(f"Sorry, you've used all of your guesses, the magic number was {magic_number}.")
        break
    elif guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("Sorry, guess again.")
    guesses -= 1