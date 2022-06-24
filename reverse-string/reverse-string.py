class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        
        while(start < end):
            temp_val1 = s[start]
            temp_val2 = s[end]
            s[start] = temp_val2
            s[end] = temp_val1
            start += 1
            end -= 1
            
            