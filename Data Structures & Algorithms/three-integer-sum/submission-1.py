class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i, val in enumerate(nums):
            if val > 0: #sorted order, everything after must be pos
                break
            if i > 0 and val == nums[i - 1]: #duplicate
                continue 

            l, r = i + 1, len(nums) - 1 #2 pointer on remaining elements

            while l < r:
                s = nums[l] + nums[r] + val

                if s > 0: #sum too large
                    r -= 1
                elif s < 0: 
                    l += 1
                else: 
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 #remove duplicate potential l's
                
        return output
            

