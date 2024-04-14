def removeElement(self,nums,val):
      
       k=0;
       for i in range(len(nums)):
           if(nums[i]!=val):
             nums[k] = nums[i]
             k=k+1

       return k;


num = [3,2,2,3]
val = 3
print("The number of the array elements after the removal of the value 3 is",removeElement(num,val))
   
   