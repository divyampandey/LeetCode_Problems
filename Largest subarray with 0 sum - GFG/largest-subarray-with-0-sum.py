#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_length = 0
        summation_dict = {}
        summation = 0
        for i in range(n):
            summation += arr[i]
            if summation == 0:
                length = i + 1
                if max_length < length:
                    max_length = length
            else:
                if summation in summation_dict.keys():
                    start_index = summation_dict[summation] + 1
                    end_index = i
                    length = (end_index - start_index)+1
                    if max_length < (length):
                        max_length = length
                else:
                    summation_dict[summation] = i
                
        return max_length        
                
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