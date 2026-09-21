class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        if len(nums) == 1:
            return nums[0]

        temp2, temp1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp2, temp1 = temp1, max(temp1, temp2 + nums[i])
            print ((temp2, temp1))

        return temp1