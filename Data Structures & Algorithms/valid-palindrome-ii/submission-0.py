class Solution:
    def validPalindrome(self, s: str) -> bool:
        temp = ""
        for i in range(len(s)):
            if self.isPalindrome(s[:i] + s[i+1:]):
                return True
        
        return False
    
    def isPalindrome(self, s):
        clean = "".join(c.lower() for c in s if s.isalnum())

        return clean == clean[::-1]