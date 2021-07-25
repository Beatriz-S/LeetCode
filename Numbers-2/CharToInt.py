'''
Purpose: Practice ASCII conversions
 

Problem Statement:
Write a program that takes a single upper case letter as input and prints its position 
number in alphabet sequence.

Criteria:
Test #	Input	Output
 1	      A	      1
 2	      L	      12

'''


x=input()
print(ord(x))
b=ord(x)-ord('A')+1
print(b)