'''
Purpose: 
Simple arithmetic operations like modulus and rounding.

Problem Statement:
Given a year (as a positive integer), find the respective number of the century. 
Note that, for example, 20th century began with the year 1901.
'''
import math

x=int(input())
result=x/100
print(math.ceil(result))