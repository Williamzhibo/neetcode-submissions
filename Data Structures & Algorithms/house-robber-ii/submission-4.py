class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robRange(lo, hi):
            house2 = house1 = 0

            for i in range(lo, hi):
                house2, house1 = house1, max(house1, house2 + nums[i]) #either two previous house, and the next one, or just the previous house

            return house1
        
        return max(robRange(0, len(nums) - 1), robRange(1, len(nums)))
        