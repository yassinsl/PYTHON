"""
Author: YASSINE LAHSSINI
Date: 16/01/2024
Time: 11:15
"""
import random
Draw_HG = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random

word_pjc = ['banana', 'apple', 'orange']
gues = random.choice(word_pjc)
word_guess = list(set(gues.replace(',', '')))

word = ['_'] * len(word_guess)
attempts = 0

while attempts < len(Draw_HG) - 1:
    guess_letter = input("Please guess a letter of the word (fruit): ").lower()

    if guess_letter in word_guess:
        for i in range(len(word_guess)):
            if guess_letter == word_guess[i]:
                word[i] = guess_letter

        print(" ".join(word))
    else:
        print(Draw_HG[attempts])
        attempts += 1

    if word == word_guess:
        print("Congratulations! You guessed the word:", "".join(word))
        break

if attempts == len(Draw_HG) - 1:
    print("Sorry, you ran out of attempts. The word was:", "".join(word_guess))
