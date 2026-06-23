class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def backtrack(start, total):
            if total == 0:
                res.append(subset.copy())
                return
            if total > target or start >= len(candidates):
                return
            candidate = candidates[start]
            subset.append(candidate)
            backtrack(start + 1, total - candidate)
            subset.pop()

            while start + 1 < len(candidates) and candidate == candidates[start + 1]:
                start += 1
            
            backtrack(start + 1, total)

        backtrack(0,target)
        return res
