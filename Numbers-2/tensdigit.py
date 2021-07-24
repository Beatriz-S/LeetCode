'''
Purpose:  
Numbers, modulus and remainder operators.

Problem Statement:
Given an integer, print its tens digit.

Criteria:
Test #	Input	Output
 1	      1	      0
 2	    1000000	  0
 3  	987	      8
 4	    73	      7
 5  	1234	  3
 6	    10	      1

'''
#receive input as integer
#divide the input by 10 and obtain its remainder
#print result

#input as int
digit=int(input())
#divide digit by tens place
result=(digit//10)%10
#print result
print(result)