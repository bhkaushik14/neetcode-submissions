class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        self.recurse("(", n, 1, 0)

        return self.result

    def recurse(self, s, n, curr_open, curr_closed):
        if len(s) == 2*n:
            self.result.append(s)
        else:
            if curr_open < n:
                self.recurse(s + "(", n, curr_open + 1, curr_closed)
            if curr_closed < n and curr_open > curr_closed:
                self.recurse(s + ")", n, curr_open, curr_closed + 1)
        
        print(s)
