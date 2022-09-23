'''
@Author: Praful Rakhade

@Date: 03-09-2022

@Last Modified by: -

@Title : 2D array of integers and doubles from standard input
         and printing them out to standard output.
'''

from array import *
print("2 D array for Integer")
row = int(input("Enter the Number of Rows: "))
column = int(input("Enter the Number of Column: "))
sum = 0
mat = []

for i in range(0, row):
    mat.append([])

for i in range(0, row):
    for j in range(0, column):
        mat[i].append([j])
        mat[i][j] = 0
print((mat))

for i in range(0, row):
    for j in range(0, column):
        print("Entry of Rows", i + 1, "Column",j + 1)
        mat[i][j] = int(input())
print((mat))

print("Matrix form :")
for i in mat:
    for j in i:
        print(j, end="\t")
    print()
print("\n")

print("2 D array for Double")
row =  int(input("Enter the Number of Rows: "))
column = int(input("Enter the Number of Column: "))
sum = 0
mat = []
for i in range(0, row):
    mat.append([])

for i in range(0, row):
    for j in range(0, column):
        mat[i].append([j])
        mat[i][j] = 0
print((mat))

for i in range(0, row):
    for j in range(0, column):
        print("Entry of Rows", i + 1, "Column",j + 1)
        mat[i][j] = float(input())
print((mat))

print("Matrix form :")
for i in mat:
    for j in i:
        print(j, end="\t")
    print()