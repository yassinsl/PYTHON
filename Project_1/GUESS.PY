"""
Author: YASSINE LAHSSINI
Date: 24/01/2024
Time: 04:59
"""

import pic_geuss
import random

print("*" * 87)
print(pic_geuss.pic_geuss)
print("*" * 87)

print("Let me think of a number between 1 and 100!")

guess_pc = random.randint(1, 100)

choose = input("Choose difficulty level ('easy' or 'hard'): ")
number_of_attempts = 10 if choose.lower() == "easy" else 5

while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number")
    guess_input = int(input("Please enter your guess: "))

    if guess_input > guess_pc:
        print("Your guess is too high!")
    elif guess_input < guess_pc:
        print("Your guess is too low!")
    elif guess_input == guess_pc:
        print("Congratulations! Your guess is correct!")
        break

    number_of_attempts -= 1

else:
    print(f"Sorry, you've run out of attempts. The correct answer was {guess_pc}. Better luck next time!")
