class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counterS = {}
        for l in s:
            counterS[l] = counterS.get(l, 0) + 1
        
        counterT = {}
        for l in t:
            counterT[l] = counterT.get(l, 0) + 1

        for l in s:
            if counterT.get(l, 0) != counterS.get(l, 0):
                return False
        
        return True

        
        