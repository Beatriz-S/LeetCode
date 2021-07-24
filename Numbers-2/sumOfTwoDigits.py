'''
Purpose: 
Numbers, modulus and remainder operations.

Problem Statement:
Given a three-digit number. Find the sum of its digits without using string operations.

Note: this problem has been solved following the UMPIRE technique as a video walk through at the end of this section.

Criteria:
Test #	Input	Output
 1	    483	    15
 2	    999	    27
 3	    100	    1
 4	    829	    19
 5	    179	    17
 6	    123	    6
'''
#receive input
digit=input()

sum = 0
for digit in str(digit):
  sum += int(digit)
  
print(sum)