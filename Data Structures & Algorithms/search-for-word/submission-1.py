class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        found = False
        def dfs(r, c, cur):
            nonlocal found
            if cur == word:
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited:
                return False

            cur += board[r][c]

            visited.add((r,c))
            found = (
                dfs(r + 1, c, cur) or
                dfs(r - 1, c, cur) or
                dfs(r, c + 1, cur) or
                dfs(r, c - 1, cur) or 
                found
            )
            visited.remove((r,c))

            return found
        for row in range(ROWS):
            for col in range(COLS):
                if word[0] == board[row][col]:
                    dfs(row, col, "")
        return found