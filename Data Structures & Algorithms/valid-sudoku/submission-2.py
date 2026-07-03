class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkValid(board) == False:
            return False
        
        cols = [list(col) for col in zip(*board)]
        if self.checkValid(cols) == False:
            return False

        blocks = []
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                curr_block = [board[i][c:c+3] for i in range(r, r+3)]
                blocks.append(curr_block[0] + curr_block[1] + curr_block[2])

        if self.checkValid(blocks) == False:
            return False
        return True
                


    def checkValid(self, twoDL):
        if len(twoDL) != 9:
            return False
        for l in twoDL:
            l = [int(w) for w in l if w != "."]
            if len(l) != len(set(l)):
                return False
            for n in l:
                if n > 9 or n < 1:
                    return False

        return True


