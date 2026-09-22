class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)  == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        house2, house1 = nums[0], max(nums[0], nums[1])

        
        #because it is circular, we either include the first, or last element in our array

        for i in range(2, len(nums) - 1):
            house2, house1 = house1, max(house1, house2 + nums[i])
        temp = house1


        house2, house1 = nums[1], max(nums[1],nums[2])
        for i in range(3, len(nums)):
            house2, house1 = house1, max(house1, house2 + nums[i])

        return max(house1, temp)
        