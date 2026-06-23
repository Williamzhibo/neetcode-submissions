class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        rowlen, collen = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        #we wish to do multi-source BFS, meaning we will enqueue all treasures
        #at the exact same time 

        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == 0:
                    q.append((r,c)) #enqueue all treasures at the same time, give them all the same depth

        while q:
            row, col = q.popleft() #remember bfs uses queue, dfs uses stack
            newDepth = grid[row][col] + 1
            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if ( 0<=nr<rowlen and 0<=nc<collen and grid[nr][nc] == INF ):
                    #valid position, and its unseen land 
                    q.append((nr, nc))
                    grid[nr][nc] = newDepth

