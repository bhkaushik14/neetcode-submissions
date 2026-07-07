class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        bracket_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in bracket_map:
                top_c = stack.pop() if stack else '#'

                if bracket_map[c] != top_c:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
