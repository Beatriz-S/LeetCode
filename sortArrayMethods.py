
def sort(A):
    for i in range(len(A)):
        minInd=i
        for j in range(i+1, len(A)):
            if A[minInd]>A[j]:
                minInd=j
    #swap the found minimum lement with
    #the first element
    A[i], A[minInd]=A[minInd],A[i]

    return A



if __name__ == '__main__':
    A=[5,4,3,2,1,0]
    print(sort(A))