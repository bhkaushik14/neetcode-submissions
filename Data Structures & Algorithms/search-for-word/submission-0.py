# Aided with GPT

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, idx):
            # Found every character
            if idx == len(word):
                return True

            # Invalid position
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # Already used this cell
            if (row, col) in visited:
                return False

            # Wrong character
            if board[row][col] != word[idx]:
                return False

            # Choose this cell
            visited.add((row, col))

            # Explore four directions
            found = (
                dfs(row + 1, col, idx + 1) or
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1)
            )

            # Backtrack
            visited.remove((row, col))

            return found

        # Try every starting position
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False