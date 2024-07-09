#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
print('Welcome to the Number guessing Game!\nI am think of a number between 1 to 100.')

answer = random.randint(1,100)
print(f"{answer} is answer")

difficulty_mode = input('Choose a difficulty. type "hard" or "easy" ')

def guessing():
    global lives
    guess = int(input('Make a guess '))
    if lives == 1:
        print('you run out of guesses, you lose')
    else:
        if guess > answer:
            print('Too high\nGuess again.')
            lives -=1
            print(f'You have {lives} attempts remaining to guess the number.')
            guessing()
        elif guess < answer:
            print('Too low\nGuess again.')
            lives -=1
            print(f'You have {lives} attempts remaining to guess the number.')
            guessing()
        else:
            print(f"you got it answer is {answer}")
    

if difficulty_mode == "hard":
    lives = 5
    print(f'You have {lives} attempts remaining to guess the number.')
    guessing()
else:
    lives = 10
    print(f'You have {lives} attempts remaining to guess the number.')
    guessing()
    