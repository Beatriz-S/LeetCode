
def twoSum(nums,target):
   #Initialize out_list
   outList=[]
   #loop throuhg the list to get the first number
   #from zero to end
   for i in range(len(nums)):
      first_num=nums[i]
      #loop through the second loop to get second number
      for j in range(i+1,len(nums)):
         second_num=nums[j]
      #if first_num+second_num==target
         if(first_num+second_num==target):
            #add the result to out_list
            outList.append(i)
            outList.append(j)
   return outList

if __name__=="__main__":
    digits=[2,7,11,15]
    print(twoSum(digits,9))
   