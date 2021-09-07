#user name as string
userName=input()
letter=userName[-1]

#char to int
num=ord(letter)
backToLetter=str(num)
#print(backToLetter[0])

ones=int(backToLetter[1])%2
tens=int(backToLetter[0])%2
print(ones, tens)
#value1=bin(ones)
#value2=bin(tens)
#print(value1,value2)
if(ones==tens):
  print('Lsb matches:', ones, tens)
else:
  print('Lsb does not match:', ones, tens)