'''
@Author: Praful Rakhade

@Date: 02-09-2022

@Last Modified by: -

@Title : User Input and Replace String Template "Hello <<UserName>>, Howare You ?."

'''

user_Name = '''"Hello <<UserName>>, How are You ?"'''

name = input("Enter the User Name :")
user_Name = user_Name.replace("<<UserName>>", name)
print(user_Name)
