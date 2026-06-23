class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(start, total):
            if total == 0:
                res.append(subset.copy())
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if num <= total:
                    subset.append(num)
                    dfs(i, total - num)
                    subset.pop()

        dfs(0, target)
        return res