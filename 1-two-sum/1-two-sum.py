class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}
        for i,num in enumerate(nums):
            f = target - num
            if f in num_index_dict.keys():
                return [i,num_index_dict[f]]
            else:
                num_index_dict[num] = i
        
             
        