'''
Original Problem Statement: 
Write a program that takes in the user's name, which is taken in as input in all lower-case characters. 
If the least significant bit of the ten's place digit of the ASCII representation of the last character of the 
name matches with the least significant bit of the one's place digit of the ASCII representation of the last character, 
print "Lsb matches: <tens lsb> <ones lsb>, otherwise print "Lsb does not match: <tens lsb> <ones lsb>".
 

Bug #	Code Line #	Bug Fix
  1	        2	
  2	        5	
  3	        12	
 
'''

user_input = input()
letter = user_input[len(user_input)-1] 
 
 
tens_place = ((ord(letter)%10**2)//10**1)
ones_place = (ord(letter)%10)

tens_lsb = tens_place % 2
ones_lsb = ones_place % 2 

if(ones_lsb == tens_lsb): 
    print("Lsb matches: ", tens_lsb, ones_lsb) 
else: 
    print("Lsb does not match:", tens_lsb, ones_lsb)


