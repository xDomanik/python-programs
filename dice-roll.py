'''
This program lets user to simulate a random dice roll
'''
import random

def flip(randomInt):
    """Function to flip and print out the flipped dice"""
    print(f"Your dice roll is... {randomInt}")

dice_num = [1,2,3,4,5,6]
name = input("Hello! What is your name")

while True:
    try:
        answer = int(input(f"{name}, Select flip (1) or quit (2)"))
        while not (answer == 1 or answer == 2):
            answer = int(input("Please enter 1 or 2"))

        if(answer == 2):
            print("Thanks for playing!!")
            break
          
        flip(random.choice(dice_num))   
    except:
        print("Please enter 1 or 2! Thanks!!")

