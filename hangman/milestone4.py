class Hangman:
    def __init__(self, word_list=None, num_lives=5):
        self.word_list = ["apple", "banana", "orange", "grape", "kiwi"]
        self.word = random.choice(word_list)
        self.list_of_guesses = [ ]
        self.num_lives = 5
        self.word_guessed = ['_'] * len(word)

    def ask_for_input():
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            elif not guess.isalpha():
                print("Invalid input. Please enter a letter.")
            elif guess in list_of_guesses:
                print("You have already guessed that letter. Please try again.")
            else:
                check_guess(guess, word)
                list_of_guesses.append(guess)

    def check_guess(self, guess, word):
        if guess in word:
            print("Good Guess!", guess, "is in the word.")
        else:
            print("Bad Guess!", guess, "is not in the word.")

# Example usage
game = Hangman()
game.ask_for_input()
