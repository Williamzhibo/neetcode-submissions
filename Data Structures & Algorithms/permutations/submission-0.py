class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, lst):
            if i >= len(nums):
                res.append(lst.copy())
                return
            num = nums[i]
            for j in range(len(lst) + 1):
                lst.insert(j, num)
                backtrack(i + 1, lst)
                lst.pop(j)

        backtrack(1, [nums[0]])
        return res