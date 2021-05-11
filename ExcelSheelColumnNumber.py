def anyLengthString(column):
    #length of the string
    length=len(column)
    answer=0
    i=0
    #take one char at a time in reverse order
    # ABC
    # 012
    #-3,-2,-1
    for index in range(length-1,-1,-1):
        #convert it to asci  number
        num = (ord(column[index])-64)
        #answer=answer plus num times 26 raised to the power of i
        answer=answer+num*(26**i)
        i+=1
    return answer