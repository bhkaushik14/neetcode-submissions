class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        parent_directory = ""

        for s in path:
            if s == "." or s == "":
                pass
            elif s == "..":
                if stack:
                    parent_directory = stack.pop()
            else:
                stack.append(s)
            
        
        output = ""
        for s in stack:
            output += "/" + s
        
        if len(stack) == 0:
            return "/"
        return output
        
        