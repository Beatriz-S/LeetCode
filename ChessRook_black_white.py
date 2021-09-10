
'''
Problem Statement: 
Given two squares of a chessboard. 
If they are painted in the same color, print YES, otherwise print NO.

The program receives four integers from 1 to 8, each specifying the column and row number, f
irst two - for the first square, and then the last two - for the second square.
'''
col=int(input())
row=int(input())
colT=int(input())
rowT=int(input())

if((col%2==0) and (row%2==0)):
  if((colT%2==0) and (rowT%2==0)):
    print('YES')
  else:
    print('NO')
elif(col%2==0 and row%2!=0):
  if(colT%2==0 and rowT%2!=0):
    print('YES')
  else:
    print("NO")
elif((col%2!=0) and (row%2!=0)):
  if((col%2!=0) and (row%2!=0)):
    print('YES')
  else:
    print('NO')
elif((col%2!=0) and (row%2==0)):
  if((colT%2!=0) and (rowT%2==0)):
    print('YES')
  else:
    print("NO")