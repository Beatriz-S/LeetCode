'''
Purpose: Practice two-digit integer problems

Problem Statement: Given a two-digit integer, print its left digit (a tens digit) and then its right digit (a ones digit).
Use the operator of integer division for obtaining the tens digit and the operator of taking remainder for obtaining the ones digit
'''
def twoDigits(n):
    x=int(n)
    bits=[0]*x
    
    #counter
    i=0
    
    while(x>0):
        bits[i]=x%10
        x=int(x/10)
        i+=1
        
    for j in range(i-1,-1,-1):
        print(bits[j],end=' ')

if __name__ == '__main__':
    n=54
    twoDigits(n)