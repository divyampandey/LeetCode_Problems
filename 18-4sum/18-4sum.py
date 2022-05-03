class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        left_pointer = 0
        right_pointer = 0
        length = len(nums)
        ans_array = []
       # [1,0,0,1,2,4,6] [8]
       # Sort the array
        nums = sorted(nums)
        for i in range(length):
            for j in range(i+1,length):
                left_pointer = j+1
                right_pointer = length - 1
                tofind = target - (nums[i] + nums[j])
                while left_pointer < right_pointer:
                    if (nums[left_pointer] + nums[right_pointer]) == tofind:
                        ans_array.append([nums[i],nums[j],nums[left_pointer],nums[right_pointer]])
                        left_val = nums[left_pointer] 
                        right_val = nums[right_pointer]
                        left_pointer += 1
                        right_pointer -= 1
                        while(left_pointer < length and nums[left_pointer]==left_val ):
                            left_pointer += 1
                        while(right_pointer > -1 and nums[right_pointer]==right_val ):
                            right_pointer -= 1
                    
                    elif nums[left_pointer] + nums[right_pointer] < tofind:
                        left_val = nums[left_pointer] 
                        left_pointer += 1
                        while(left_pointer < length and nums[left_pointer]==left_val):
                            left_pointer += 1
                    
                    else:
                        right_val = nums[right_pointer]
                        right_pointer -= 1
                        while(right_pointer > -1 and nums[right_pointer]==right_val):
                            right_pointer -= 1
                            
        ans_array = sorted(ans_array)
        ans_array = [k for k,_ in itertools.groupby(ans_array)]
        return ans_array                                
                                          
                
                
        