import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)): 
            #euclidean distance from 0, store dist + index
            heapq.heappush( minHeap, ( math.sqrt( (points[i][0]**2) + (points[i][1]**2) ) , i) )
        res = [] 

        print (minHeap)
        for j in range(k):
            res.append( points[heapq.heappop(minHeap)[1]] )

        return res
