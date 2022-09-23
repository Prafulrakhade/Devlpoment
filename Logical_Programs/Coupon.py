'''
@Author:- Praful Rakhade

@Date:- 03-09-2022

@Last Modified by:-

@Title :- a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
             need to generate distinct coupon number? This program simulates this random
             process.
          b. I/P -> N Distinct Coupon Number
          c. Logic -> repeatedly choose a random number and check whether it's a new one.
          d. O/P -> total random number needed to have all distinct numbers.
          e. Functions => Write Class Static Functions to generate random number and to
             process distinct coupons.

'''
import random

length = 10
for i in range(length):
    num = 0
    r1 = random.randint(0, 9)
    num = num+r1
    print(num, end="")
