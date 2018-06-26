"""
The Goal: Similar to the first project, this project also uses the random 
module in Python. The program will first randomly generate a number unknown to 
the user. The user needs to guess what that number is. (In other words, the 
user needs to be able to input information.) If the user's guess is wrong, the 
program should return some sort of indication as to how wrong (e.g. The number 
is too high or too low). If the user guesses correctly, a positive indication 
should appear. You'll need functions to check if the user input is an actual 
number, to see the difference between the inputted number and the randomly 
generated numbers, and to then compare the numbers.

Concepts to keep in mind:
- Random function
- Variables
- Integers
- Input/Output
- Print
- While loops
- If/Else statements
"""

import random

def play():
    attempt = 1
    random_num = random.randrange(1, 11)
    user_choice = int(raw_input("Choose a number between 1 and 10: "))

    while attempt < 5:
        if user_choice == random_num:
            print "You win!"
            break
        else:
            user_choice = int(raw_input("Wrong! Try again: "))
            attempt += 1

while True:
    user_answer = str(raw_input("Would you like to play a game? [y/n] "))
    if user_answer.lower() == "y":
        play()
    else: 
        print("Fine! Don't play then!")
        break
