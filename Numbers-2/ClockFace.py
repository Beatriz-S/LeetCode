'''
Purpose: 
To practice remainder and integer division operations.

Problem Statement:
The hour hand of an analog clock turned α degrees since the midnight. 
Determine and print the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.
'''
import math

min=input()
result=((float(12)*float(min))/360)

r=int(min)-180
rule=(int(min)%30)*12
print(rule)