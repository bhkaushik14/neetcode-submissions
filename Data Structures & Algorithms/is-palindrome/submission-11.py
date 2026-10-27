class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (c := ''.join(filter(str.isalnum, s.lower()))) == c[::-1]
