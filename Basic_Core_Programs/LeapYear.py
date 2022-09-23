'''
@Author: Praful Rakhade

@Date: 02-09-2022

@Last Modified by: -

@Title : find the year is leap or not.

'''

year = int(input("Enter the Year : "))

while year < 999 or year > 9999:
    print("Wrong Input")
    print("inter year in 4 digits")
    year = int(input("Enter the Year : "))

if(year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
    print(year , "is a Leap Year")
else:
    print(year , "is not Leap Year")
