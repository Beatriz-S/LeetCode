'''
Purpose: Practice ASCII conversions
 

Problem Statement:
Write a program that takes two upper case letters as input and prints its position number in alphabet sequence, [A, B, C, .... X, Y, Z, AA, AB, AC, AD .... AX, AY, AZ, ... ZX, ZY, ZZ]

Criteria:
Test #	Input	Output
 1	     AA	    (26 * 1) + 1 = 27
 2	     AB	    (26 * 1) + 2 = 28
 3	     KE	    (26 * 11) + 5 = 291
''' 
word=input()
#ord is used to obtain the ascii value of the first char
#subtract A=65 to obtain the differnce and add one to the 
# result to obtain the actualian numerical value of the char
#the result is then multiplied by 26 (26 letters of alphabet)
firstLetter=((ord(word[0])-ord('A')+1) * 26)
#ord is used to obtain the ascii value of the second char
#subtract A=65 to obtain the differnce and add one to the 
# result to obtain the actualian numerical value of the char
#the result is then multiplied by 26 (26 letters of alphabet)
secondLetter=((ord(word[1])-ord('A')+1))
#add both result to obtain the actual value for both chars
letter=firstLetter + secondLetter
print(letter)