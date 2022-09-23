'''
@Author: Praful Rakhade

@Date: 03-09-2022

@Last Modified by: -

@Title : Take a command line argument N and a print table
         of the power of 2 that are less tahn or equal to 2^N.

'''

val = 1
pwr = int(input("Enter to find power of 2 : "))
while pwr > 32:
    print("Invalid Input")
    print("Enter value is less than 32:")
    pwr = int(input("Enter to find power of 2 less than 32: "))

for i in range(1, pwr + 1):
    val = val * 2
    print(val)