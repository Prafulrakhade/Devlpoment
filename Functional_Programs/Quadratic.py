'''
@Author:- Praful Rakhade

@Date:- 03-09-2022

@Last Modified by:-

@Title :- rite a program Quadratic to find the roots of the equation a*x*x + b*x + c.
          can be found using a formula (Note: Take a, b and c as input values)
          Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
          delta = b*b - 4*a*c
          Root 1 of x = (-b + sqrt(delta))/(2*a)
          Root 2 of x = (-b - sqrt(delta))/(2*a).

'''
from cmath import sqrt

a = int(input("Enter the Value of a : "))
b = int(input("Enter the Value of b : "))
c = int(input("Enter the Value of c : "))
delta = (b ** 2) - (4 * a * c)
result1 = (-b + sqrt(delta)) / (2 * a)
result2 = (-b - sqrt(delta)) / (2 * a)
print("root1 ", result1, "root2", result2)
