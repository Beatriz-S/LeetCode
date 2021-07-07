

def plusOne(digits):
   i=len(digits)-1
   #initiallizing an out list
   out=[]
   #initialize variable temp= digits[i]+1
   temp = digits[i] + 1
   while(True):
      #if(tempt==10)
      #insert 0 on the top of out
      #set carry=1
      if(temp == 10):
         out.insert(0, 0)
         carry=1
      else:
         out.insert(0, temp)
         carry=0
         
      #decrement i
      i = i - 1
      if(i<0):
         break
      #calculate temp=digits[i]+carry
      temp=digits[i]+carry
      
      #go back to 4
   return out
      
    
    
if __name__ == '__main__':
    n=[1,2,3]
    print(plusOne(n))
      