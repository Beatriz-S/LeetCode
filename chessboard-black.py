


if __name__ == '__main__':
    x=int(input())
    y=int(input())
#ifx.y are even. Print YES
    if((x%2==0) and (y%2==0)):
        print('YES')
    #if both are odd. print YES
    elif((x%2!=0) and (y%2!=0)):
        print('YES')
    else:
        print('NO')
