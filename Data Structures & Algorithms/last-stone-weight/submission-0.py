#we want a heap(?) to store our largest k elements -- stones 
#the goal should be to continually re-heapify? but that is nlogn operations... not super ideal 
# 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [- x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones) #bigger
            stone2 = heapq.heappop(stones) #smaller 

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        if (stones):
            return - stones[0]    
        return 0

