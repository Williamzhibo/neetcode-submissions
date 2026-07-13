class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inverse = [ - num for num in nums]
        heapq.heapify(inverse)

        for i in range(k - 1):
            heapq.heappop(inverse)

        return - heapq.heappop(inverse)