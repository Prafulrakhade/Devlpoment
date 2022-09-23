'''
@Author:- Praful Rakhade

@Date:- 03-09-2022

@Last Modified by:-

@Title :- Write a program WindChill.java that takes two double command-line arguments t
          and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
          temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
          National Weather Service defines the effective temperature (the wind chill) to be:
          w = 35.74 + 0.6215t + (0.4275t-35.75)v0.16
'''
import math
v = float(input("Enter the Wind Speed : "))
t = float(input("Enter the temperature : "))

result = 35.74 + 0.6215 *t + (0.4275 *t -35.75) *math.pow(v, 0.16)

print("The WindChil is ", int(result))
