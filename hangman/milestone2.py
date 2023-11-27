import random


fruits = ["apple", "banana", "orange", "grape", "kiwi"]

word_list = fruits
word = random.choice(word_list)
guess = input("Guess a letter: ")


if len(guess) != 1:
print("Invalid input. Please enter a single letter.")
elif not guess.isalpha():
print("Invalid input. Please enter a letter.")
elif guess in word:
print("Correct!")
else:
print("Incorrect.")
       

        
        