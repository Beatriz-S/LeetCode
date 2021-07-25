'''
Purpose: If/else statements
 

Problem Statement:
Given two input numbers, print 'True' if the last least significant bit of the two number match and 'False' if they don't.

Test #	Input	Output
  1	     3 5	True (because 3 is 0b11 and 5 if 0b101 - the lsb is 1 in both)
  2	     6 8	True (because 6 is 0b110 and 8 is 0b1000 - the lsb is 0 in both
  3    	 5 8	False (because 5 is 0b101 and 8 is 0b1000 - the lsb is not the same

'''

x=input()
#store input as a list
lstuser=x.split() #separates the values by space
#turning the int int a bit
one=(int(lstuser[0])&1)
two=(int(lstuser[1])&1)
#print(one , int(lstuser[0]))
#print(two, int(lstuser[1]))
if(one == two):
  print('True')
else:
  print('False')

#other ways to output the significant bit is by
#doing one=int(lstuser[0])%2
#two=int(lstuser[1])%2

#one=bin(int(lstuser[0]))
#two=bin(int(lstuser[1]))
#lsb1=one[-1]
#lsb2=two[-1]