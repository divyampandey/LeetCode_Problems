class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       # print(nums)
        i = 1
        j = 0
        
        while(i < len(nums)):
            tempi = nums[i]
            tempj = nums[j]
           # print(tempi,tempj)
            if tempi < tempj:
                t = i-1
                while(t >=0 and tempi < nums[t]):
                    nums[t+1]=nums[t]
                  #  print(nums)
                 #   print('inside^^^^^^')
                    t = t - 1

                t = t + 1
                nums[t]=tempi
                #print(nums)
               # print("outside-----")
            j= j + 1
            i= i+1
        
        
