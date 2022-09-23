
'''
@Author:- Praful Rakhade

@Date:- 03-09-2022

@Last Modified by:-

@Title :- Write a program 'Distance' that takes two integer command-line arguments x
          and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
          formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function.

'''

import math

x=int(input("Enter the first Number : "))
y=int(input("Enter the Second Number : "))

Dist=math.sqrt(x * x + y * y)

print("Distance between ", x," and", y," is", Dist)