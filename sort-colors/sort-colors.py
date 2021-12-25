class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                count_2 += 1
        
        length = 0
        while (length != len(nums)):
            if count_0 > 0:
                nums[length] = 0
                count_0 -= 1
                length += 1
            elif count_1 > 0:
                nums[length] = 1
                count_1 -= 1
                length += 1
            else:
                nums[length] = 2
                count_2 -= 1
                length += 1
                
        
        
