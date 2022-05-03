#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        # [15, -2, 2, -8, 1, 7, 10, 23]
        summation = 0
        max_length_of_subarray = 0
        summation_dict = {}
        for index,number in enumerate(arr):
            #print(max_length_of_subarray)
            summation += number
            #print(summation)
            if summation == 0:
                start_index = 0
                end_index = index
                len_of_subarray = (end_index - start_index)+1
                if max_length_of_subarray < len_of_subarray:
                    max_length_of_subarray = len_of_subarray
            
            if summation in summation_dict.keys():
                start_index = summation_dict[summation] + 1
                end_index = index
                len_of_subarray = (end_index - start_index) + 1
                if max_length_of_subarray < len_of_subarray:
                    max_length_of_subarray = len_of_subarray
                
                #print(start_index,end_index, len_of_subarray, max_length_of_subarray)
            
            else:
                summation_dict[summation] = index
        
        return max_length_of_subarray

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends