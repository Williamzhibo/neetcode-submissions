class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        output.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (- nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            output.append(-heap[0][0])

        return output
