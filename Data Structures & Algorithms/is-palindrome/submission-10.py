class Solution:
    def isPalindrome(self, s: str) -> bool:
        fresh = "".join(c.lower() for c in s if c.isalnum())
        return fresh == fresh[::-1]

