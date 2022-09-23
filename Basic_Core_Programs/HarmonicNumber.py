'''
@Author: Praful Rakhade

@Date: 03-09-2022

@Last Modified by: -

@Title : Print the Nth Harmonic Number: 1/2 + 1/3 + .... + 1/N.

'''
import math
from tokenize import Double

result = 0
num = int(input("Enter the Number:"))
for i in range(1, num+1):
    result = result + 1/i
    print("Harmonic Number of", i, "is ",result)

