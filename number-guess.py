'''
This program lets user set lower & top tier number and select a number between them!
'''
import random

#init var
name = input("Please enter your fullname!\n")
lower = input(f"{name} Please enter you min number?\n")
high = input(f"{name} Please enter your max number?\n")
correctNUm = random.randrange(int(lower), int(high) + 1 )

def userGuess(correctNum):

print(f"{name} {lower} {high}")

