class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict1 = {}
        for l in s:
            dict1[l] = dict1.get(l, 0) + 1
        
        dict2 = {}
        for l in t:
            dict2[l] = dict2.get(l, 0) + 1

        for l in s:
            if dict1.get(l, 0) != dict2.get(l, 0):
                return False
        return True
        
        
        