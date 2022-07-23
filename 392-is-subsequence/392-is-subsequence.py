class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        length = len(s)
        i = 0
        for character in t:
            if s[i] == character:
                i += 1
                if i == length:
                    return True
            

        return False