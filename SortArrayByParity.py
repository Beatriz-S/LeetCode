class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in nums:
            if(i%2)==0:
                even.append(i)
            elif(i%2)!=0:
                odd.append(i)
        result=[]    
        result=even+odd
        return result
    
'''
result=[]
        for i in nums:
            if(i%2 == 0):
                result.append(i)
        for i in nums:
            if(i%2 != 0):
                result.append(i)
                '''