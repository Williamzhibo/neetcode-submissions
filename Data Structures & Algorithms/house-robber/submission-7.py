class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        house2 = house1 = 0

        for i in range(0, len(nums)):
            house2, house1 = house1, max(house2 + nums[i], house1)
        return house1