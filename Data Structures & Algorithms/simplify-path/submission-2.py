class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        for s in path:
            if s == "." or s == "":
                pass
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
            
        
        return "/" + "/".join(stack)
        
        