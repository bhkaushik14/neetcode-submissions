class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        check_t = {}
        window = {}

        for c in t:
            check_t[c] = check_t.get(c, 0) + 1
        
        have, need = 0, len(check_t)
        result, resultLen = [-1, -1], float("infinity")
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in check_t and window[c] == check_t[c]:
                have += 1
                
            while have == need:
                if r - l + 1 < resultLen:
                    result = [l, r]
                    resultLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in check_t and window[s[l]] < check_t[s[l]]:
                    have -= 1
                l += 1
        return s[result[0]:result[1] + 1] if resultLen != float("infinity") else ""



