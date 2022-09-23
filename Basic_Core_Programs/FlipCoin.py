'''
@Author: Praful Rakhade

@Date: 02-09-2022

@Last Modified by: -

@Title : Flip Coin and and print percentage of Heads and Tails.


'''

import random

heads = 0
tails = 0
numOfFlips = int(input("Enter the number of times you want to flip coin :"))

for i in range(numOfFlips):
    rdm = random.randint(0, 1)
    if( rdm < 0.5):
        heads = heads + 1
    else:
        tails = tails + 1
print("Percentage of Heads = ",float(heads / numOfFlips) * 100,"%")
print("Percentage of Tails = ",float(tails / numOfFlips) * 100,"%")