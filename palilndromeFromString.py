

def tokenizeString(self):
    s='abcda'
    queries=[[3,3,0],[1,2,0]]

    for i in queries:
        left=i[0]
        right=i[1]
        change=i[2]
        substring=[]
        substring.append(s[left:right+1])
        
        makepalindrome(substring,change)

def makepalindrome(self, substring ,change):
    pass