class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        check_1 = {}
        for c in s:
            check_1[c] = check_1.get(c, 0) + 1
        
        check_2 = {}
        for c in t:
            check_2[c] = check_2.get(c, 0) + 1
        
        return check_1 == check_2
        

