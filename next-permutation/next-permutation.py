class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## calculate the length of the list
        length  = len(nums)
        index = length - 1
        minval = nums[index]
        minindex = index
        while(index >  0 and (nums[index] <= nums[index-1])):
            if nums[index] < minval:
                minval = nums[index]
                minindex = index
            index -= 1

        if index == -1:
            k = 0
            l = length - 1
            while(k < l):
                temp = nums[k]
                nums[k] = nums[l]
                nums[l] = temp
        
        else:
            temp = nums[index-1]
            minval = nums[index]
            minindex = index
            for z in range(index,length):
                if nums[z] > temp:
                    minval = nums[z]
                    minindex = z
            
            nums[index-1] = minval
            nums[minindex] = temp

            
            
            temp = nums[index:length]
            temp.sort()
            k = 0
            while(k!= len(temp)):
                nums[index]= temp[k]
                k+=1
                index+=1
   