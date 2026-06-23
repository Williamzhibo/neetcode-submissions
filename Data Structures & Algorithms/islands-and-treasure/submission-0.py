from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: 
            return
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Multi-source: Add all treasures to the queue initially
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        # Perform Multi-Source BFS
        while q:
            r, c, d = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if the cell is an empty room (2147483647)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))
        
        # REMOVED: return grid
        # Simply returning nothing (or return None) modifies the grid in-place
        return None