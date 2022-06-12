class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        result, max_sum = nums[0], nums[0]
        for i in range(1,length):
            temp_sum = max_sum + nums[i]
            if (nums[i] < temp_sum):
                max_sum = temp_sum
                if result < max_sum:
                    result = max_sum
            elif (nums[i] >= temp_sum):
                max_sum = nums[i]
                if result < max_sum:
                    result = max_sum
        
        return result
                
            
        