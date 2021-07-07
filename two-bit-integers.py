'''
Purpose: Practice two-bit integer problems

Problem Statement: Given a 2 bit integer, print its left bit (a 2's bit) and then its right bit (a ones bit). 
Use the operator of integer division for obtaining the 2's bit and the operator of taking remainder for obtaining the ones bit.

Criteria:
Test #	Input	Output
1	    0	    0 0
2	    1	    0 1
3	    2	    1 0

'''

def intToBit(j):
    R=j/2
    print(str(R))
    
    
    x=R//2
    print(str(x))
    



if __name__ == '__main__':
    intToBit(1)