class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            delta = target - (numbers[r] + numbers[l])

            if delta == 0:
                return [l + 1, r + 1]
            
            if delta < 0: 
                r -= 1
            if delta > 0: 
                l += 1
            
        return [l + 1, r + 1]
