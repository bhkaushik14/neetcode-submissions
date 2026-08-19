class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        l, r = 0, 0
        longest = 0

        while r < len(s):
            while s[r] in check:
                check.pop(s[l])
                l += 1
            
            check[s[r]] = 1

            if r - l + 1 > longest:
                longest = r - l + 1
            
            r += 1
        
        return longest
        