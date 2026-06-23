class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowlength = len(matrix[0]) #horizontal
        size = len(matrix) * len(matrix[0])
        def searchHelper (l, r):
            if l > r:
                return False
            mid = (l + r) // 2
            y = mid // rowlength
            x = mid % rowlength
            if (matrix[y][x] == target):
                return True
            elif (matrix[y][x] < target):
                return searchHelper(mid + 1, r)
            else:
                return searchHelper(l, mid - 1)
            
        return searchHelper(0, size - 1)