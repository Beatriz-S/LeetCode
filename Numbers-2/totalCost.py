import math

dollars=int(input())
cent=int(input())
numIce=int(input())
#mutiply cent by number of icecream
cent=cent*numIce
#multiply dollars by number of ice cream
dollars=dollars*numIce
totalDollars=0
totalCents=0
centToDollars=0

if cent >= 100:
  cent=cent/100
  #remove the decimal point
  centToDollars=math.trunc(cent)
  #print(centToDollars)

#subtract amount of cents added to centToDollars
totalCents=cent - centToDollars
#print(totalCents)
totalDollars=dollars + centToDollars
#print(totalDollars)

if centToDollars != 0:
  #totalCents=int(totalCents)
  
  print(totalDollars, totalCents)
else:
  print(totalDollars, cent)