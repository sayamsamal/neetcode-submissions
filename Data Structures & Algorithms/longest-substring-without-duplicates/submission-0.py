class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        charSet = set()

        lb = 0
        res = 0

        for rb in range(len(s)):
            while s[rb] in charSet:
                charSet.remove(s[lb])
                lb += 1
            charSet.add(s[rb])
            res = max(res, rb - lb + 1)
        
        return res