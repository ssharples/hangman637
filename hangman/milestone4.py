import random 

class Hangman:
    def __init__(self, word_list=None, num_lives=5):
        if word_list is None:
            word_list = ["apple", "banana", "orange", "grape", "kiwi"]
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.num_lives = num_lives
        self.word_guessed = ['_'] * len(self.word)

    def ask_for_input(self):
        while self.num_lives > 0 and '_' in self.word_guessed:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            elif not guess.isalpha():
                print("Invalid input. Please enter a letter.")
            elif guess in self.list_of_guesses:
                print("You have already guessed that letter. Please try again.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        print("Game over!")

    def check_guess(self, guess):
        if guess in self.word:
            print("Good Guess!", guess, "is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(' '.join(self.word_guessed))
            if '_' not in self.word_guessed:
                print("Congratulations! You've guessed the word!")
                self.num_lives = 0
        else:
            self.num_lives -= 1
            print("Bad Guess!", guess, "is not in the word. Lives left:", self.num_lives)

# Example usage
game = Hangman()
game.ask_for_input()
