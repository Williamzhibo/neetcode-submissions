class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchHelper(l, r):
            if l > r:
                return -1
            mid = r + l // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return searchHelper(mid + 1, r)
            else:
                return searchHelper(l, mid - 1)
        
        return searchHelper(0, len(nums) - 1)