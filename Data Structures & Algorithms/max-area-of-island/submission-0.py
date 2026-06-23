class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        biggestIsland = 0

        def dfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            
            area = 1
            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (not(nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0)):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    biggestIsland = max(biggestIsland, dfs(r, c))

        return biggestIsland