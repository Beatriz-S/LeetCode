'''
Purpose: Practice bitwise operators
Problem Statement:
Given five input numbers, a, b, c, d and n, print out the number of 1 bits at the nth least significant bit position in all four numbers a, b, c, d.

Criteria:
Test #	Input	Output
 1	    1 1 1 1 0	4
 2	    2 3 5 6 1	3
'''

'''
x=input()
inptLen=len(x)
print(x)
turnToList=x.split()
print('lista: ', turnToList)
print(turnToList[3])
#for i in range(x+1):

a=int(turnToList[0])
b=int(turnToList[1])
c=int(turnToList[2])
d=int(turnToList[3])
e=int(turnToList[4])

valueA=bin(a)
valueB=bin(b)
valueC=bin(c)
valueD=bin(d)
valueE=bin(e)

valueA=int(valueA,2)
valueB=int(valueB,2)
valueC=int(valueC,2)
valueD=int(valueD,2)
fvalueE=int(valueE,2)

one=int(valueA>>1)
two=int(valueB>>1)
three=int(valueC>>1)
four=int(valueD>>1)
five=int(valueE>>1)

print('bin: ',one)
'''
x=input()
z=x.split()



x=input()
#store input as a list
lstuser=x.split()
#lstuser=x.split() #separates the values by space
size=len(lstuser)
add=0
n=lstuser[-1]
dictList={0:-1, 1:-2, 2:-3, 3:-4, 5:-6}

for i in range(size -1):
   #turning the int int a bit
  bit = int(lstuser[i])
  value=bin(bit)
  #print('bit', bit)
  #print('values',value)
  #print('value -1:',value[-2])
  if(lstuser[-1]==n):
    add=add+1

print('sum',add)