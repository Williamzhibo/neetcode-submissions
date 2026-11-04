class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMax, curMin = 1, 1
        for n in nums:
            tmp = n * curMax

            curMax = max(n, tmp, curMin * n)
            curMin = min(n, tmp, curMin * n)
            result = max(result, curMax)

        return result

