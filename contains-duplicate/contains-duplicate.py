class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary= {}
        for i in nums:
            if i in dictionary.keys():
                return True
            else:
                dictionary[i] = 1
        return False