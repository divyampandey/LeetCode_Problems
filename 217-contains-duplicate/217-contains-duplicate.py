class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            else:
                return True
        
        return False