'''
@Author:- Praful Rakhade

@Date:- 03-09-2022

@Last Modified by:-

@Title :- a. Desc -> A program with cubic running time. Read in N integers and counts the
             number of triples that sum to exactly 0.
          b. I/P -> N number of integer, and N integer input array
          c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
          d. O/P -> One Output is number of distinct triplets as well as the second output is to
             print the distinct triplets.

'''
def Sum(arr, n):

    found = False
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    if (found == False):
        print(" not exist ")


arr = [0, -1, 2, -3, 1]
n = len(arr)
Sum(arr, n)
