class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, val in enumerate(nums):
            to_find = target - val
            if to_find in num_dict.keys():
                return [index,num_dict[to_find]]
            if val not in  num_dict.keys():
                num_dict[val] = index
            
            
        return -1