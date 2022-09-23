'''
@Author:- Praful Rakhade

@Date:- 02-09-2022

@Last Modified by:-

@Title : Find the Prime Factors of 'N' and print it.

'''
fact = int(input("Enter the Number to find prime Factor: "))
print("Prime factors of", fact, "=")
for i in range(2,fact):
    if(fact % i == 0):
        print(i)
