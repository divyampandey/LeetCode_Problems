class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydict = {}
        max_length = 0
        for num in nums:
            mydict[num] = True
        
        for i in range(len(nums)):
            temp_len = 1
            val = nums[i]
            prev_val = val-1
            if prev_val in mydict.keys():
                pass
            else:
                next_val = val + 1
                while(next_val in mydict.keys()):
                    temp_len += 1
                    next_val += 1
                
                if max_length < temp_len:
                    max_length = temp_len
        return max_length
        
                
            