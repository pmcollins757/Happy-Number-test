# -*- coding: utf-8 -*-
"""
This script asks for a number, expecting an integer, 
and tests to see if it is a happy number.
http://en.wikipedia.org/wiki/Happy_number
"""

num_to_test = str(input("Enter a number to see if it is happy: "))
original_num = num_to_test
square_sum = 0
square_sum_list = []
while (square_sum != 1) and (square_sum not in square_sum_list):
    square_sum_list.append(square_sum)
    square_sum = 0
    square_sum = sum((int(digit)**2 for digit in num_to_test ))
    num_to_test = str(square_sum)
if square_sum == 1:
    print("{} is happy".format(original_num))
else:
    print("{} isn't happy".format(original_num))

