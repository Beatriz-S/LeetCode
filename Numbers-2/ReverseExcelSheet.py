'''
Purpose: Practice with strings

Problem Statement:
Write a program that takes upper case letters (an Excel Column Number) as input and prints the letters in reverse order.

Criteria:
Test #	Input	Output
   1	AB	     BA
   2	EF	     FE
   3	KELM	 MLEK
   4	AAB      BAA 
'''
x=input()
#This method returns True if all characters in the string are uppercase,
#  otherwise, returns “False”.
if(x.isupper()==True):
    #Traversing the string backwards
    result=x[::-1]
    print(result)