class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_s1 = {}
        check_s2 = {}

        if len(s1) > len(s2):
            return False
        
        l = 0

        for char in s1:
            check_s1[char] = check_s1.get(char, 0) + 1

        for r in range(len(s2)):
            check_s2[s2[r]] = check_s2.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                check_s2[s2[l]] -= 1

                if check_s2[s2[l]] == 0:
                    check_s2.pop(s2[l])

                l += 1

            if check_s2 == check_s1:
                return True

        
        return False



