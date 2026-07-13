class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        current_str = ""
        current_num = 0

        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c.isalpha():
                current_str += c
            elif c == "]":
                saved_num, saved_str = stack.pop()
                current_str = saved_str + current_str * saved_num
            elif c == "[":
                stack.append((current_num, current_str))
                current_str = ""
                current_num = 0
            print(current_str, current_num, c)

        return current_str  