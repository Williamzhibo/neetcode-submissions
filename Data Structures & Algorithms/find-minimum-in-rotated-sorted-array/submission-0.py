class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = nums[0]
        while l <= r:
            mid = (l + r) // 2
            m = min(m, nums[mid])

            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return m