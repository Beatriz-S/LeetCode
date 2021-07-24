'''
Purpose: 
Numbers, modulus and remainder operations.

Problem Statement:
Given a positive real number, print its first digit to the right of the decimal point without using string operations.

Criteria:
Test #	Input	Output
 1	    5.29	    2
 2	    179.12	    1
 3	    19.99	    9
 4	    179	        0
 5	    0.001	    0
 6	    10.34	    3
 7	    1.79	    7
'''

#receive input
digit=input()
#split, splits the string from the delimiter provided and return the string of numbers after the delimiter

#if '.' is in the string 
if '.' in digit:
  this=digit.split('.',1)[1]
  #print the first number after the split
  print(this[0])
#if no period is found then print zero
else:
  print(0)



