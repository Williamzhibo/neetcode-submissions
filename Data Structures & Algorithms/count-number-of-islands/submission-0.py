class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        rows, cols = len(grid), len(grid[0])

        islands = 0 

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0" #marking a 0 is the exact same as marking visited in separate table 
            q.append((r,c))

            while q: #while our chain is nonempty, add/remove
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col
                    #ensure within bounds, and unvisited
                    if (not (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0")): 
                        q.append((nr, nc)) #add neighbors to queue, mark visited
                        grid[nr][nc] = "0" #mark it as visited
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1 
        
        return islands 


