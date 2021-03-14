'''
This program lets user set lower & top tier number and select a number between them!
'''
import random

#init var
name = input("Please enter your fullname!\n")

# Loop to check correct input
while True:

    try:
        lower = int(input(f"{name} Please enter you min number?\n"))
        high = int(input(f"{name} Please enter your max number?\n"))
    except:
        print("Numbers only! Try again")
    else:
        break

# Gets random number between two ranges: lower & upper
correctNum =  random.randrange(lower, high + 1 )

# Core Funcs
def userGuess(correctNum):
    """ Accepts user guess and compares with correct num"""

    guess = int(input(f"Input your guess between {lower} and {high}"))
    
    print(str(guess) + " this is guess value \n")

    while guess != correctNum:
        dataString = printMessage(guess, correctNum, name, -1)

        print(dataString + "\n")
        print(correctNum)
        userGuess(correctNum)
        break

    return printMessage(guess, correctNum, name, 1)

def printMessage(userGuess, correctNum, name, modifier):
    """Print the output message for the user guess on each attempt"""
    output = ""
    if(modifier > 0): 
        output = f"Great! {name} you selected the correct int: {correctNum}"
        return output
    
    # Condition on checking if guess number is too big or too small
    if userGuess < correctNum:
        output = f"{name}, Please try again! Your guess is too low\n"
        return output
    elif userGuess > correctNum:
        output = f"{name}, Please try again! your guess is too high\n"
        return output

print(userGuess(correctNum))