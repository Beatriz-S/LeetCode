'''Problem Statement: 
Chess rook moves horizontally or vertically. Given two different squares of the chessboard, determine whether a rook can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a rook can go from the first square to the second one in a single move or NO otherwise.

Example input
4 (first block column)
4 (first block row)
5 (second block column) 
5 (second block row)

Example output
NO (because the move would be diagonal) 
'''
rook1=[]
rook2=[]

for i in range(4):
  if(i<2):
    a=input("Enter the first square: ")
    rook1.append(a)
  elif(i>1 and i<4):
    b=input("Enter the first square: ")
    rook2.append(b)

#check if the second rook is the same as the first rook
#column
#check if the range is correct
if(int(rook1[0])<9 and  int(rook2[0])<9):
  #if they are the same
  if(rook1[0]==rook2[0]):
    print('YES')
  elif((rook1[0]==rook2[1])or (rook1[1]==rook2[1])):
    if(int(rook2[1])<9):
      print('YES')
    else:
      print('NO')
  else:
    print('NO')
else:print('NO')