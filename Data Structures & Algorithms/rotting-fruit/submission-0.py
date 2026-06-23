class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        rlen, clen = len(grid), len(grid[0])
        time = 0
        fresh = 0
        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 2:
                    q.append((r,c,0)) # add all rotting fruit at beginning, time = 0

                if grid[r][c] == 1:
                    fresh += 1
        
        while q:
            row, col, prev = q.popleft()
            time = max(time, prev)
            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if (0<= nr < rlen and 0 <= nc < clen and grid[nr][nc] == 1):
                    q.append((nr, nc, prev + 1))
                    grid[nr][nc] = 2 #mark all fruit rotten
                    fresh -= 1
        
        if fresh == 0:
            return time 
        else: 
            return -1