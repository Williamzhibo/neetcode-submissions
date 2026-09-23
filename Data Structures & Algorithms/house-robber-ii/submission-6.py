class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def backtrack(lo, hi):
            house2, house1 = 0,0

            for i in range(lo, hi):
                house2, house1 = house1, max(house2 + nums[i], house1) #choose bigger of the two
                # pointers represent max of the robable houses up to this house
            return house1
        
        return max(backtrack(0, len(nums) - 1), backtrack(1, len(nums)))


