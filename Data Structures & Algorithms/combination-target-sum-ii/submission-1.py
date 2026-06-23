class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        def backtrack(index, target):
            if target == 0 and subset not in res:
                res.append(subset.copy())
                return
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if candidate <= target:
                    subset.append(candidate)
                    backtrack(i + 1, target - candidate)
                    subset.pop()
        backtrack(0,target)
        return res