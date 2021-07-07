class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_list=[]
        odd_list=[]
        
        for i in A:
            if i%2 ==0:
                even_list.append(i)
            elif i%2!=0:
                odd_list.append(i)
                
        result=even_list + odd_list
        return result
        