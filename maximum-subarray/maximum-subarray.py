class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp_sum = 0
        
        for i in nums:
            if temp_sum <= 0:
                temp_sum = i
            else:
                temp_sum += i
            
            if temp_sum > max_sum:
                max_sum = temp_sum
        
        return max_sum
            