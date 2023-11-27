

def ask_for_input():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter.")
        else:
            return guess

def check_guess(guess, word):
    if guess in word:
        print("Good Guess!", guess, "is in the word.")
    else:
        print("Bad Guess!", guess, "is not in the word.")


guess = ask_for_input()
check_guess(guess, word)

