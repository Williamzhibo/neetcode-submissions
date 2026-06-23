class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start, target):
            if target == 0:
                res.append(subset.copy())

            for i in range(start, len(nums)):
                num = nums[i]
                if num <= target:
                    subset.append(num)
                    backtrack(i, target - num)
                    subset.pop()
        backtrack(0, target)
        return res      