'''
Purpose: Practice with bitwise operators
 

Problem Statement:
Given two input numbers, print out the two numbers with their binary value shifted to the right by 1 bit.

Criteria:
Test #	Input	Output
  1	    3  5	  1 2
  2	    6 8	    3 4
  3	    5 8	    2 4

'''

x=input()
#store input as a list
lstuser=x.split() #separates the values by space
#turning the int int a bit
one = int(lstuser[0])
two = int(lstuser[1]) 

value1=bin(one)
value2=bin(two)
#value1='1'
#vallue1 to base 2
binToint=int(value1,2)
binToint2=int(value2,2)

print(binToint>>1,binToint2>>1)