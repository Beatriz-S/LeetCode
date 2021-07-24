'''
Problem Statement:
Given an integer greater than 9, print its last two digits in the reverse order, 
1's value first, and then 10's value with a space in between.

Criteria:
Test #	Input	Output
    1	1234	4 3
    2	567	    7 6
    3	64  	4 6
    4	82649	9 4
    5	182310	0 1
'''
#get user input
#num=int(input())
num=str(input())
#initialize the reverse num
revNum=0
#making num into a list
num=list(num)
#reverse works with lists
num.reverse()
num=''.join(num)

print(num[0] , num[1])

#use print(*num) to print the list with space separated elements