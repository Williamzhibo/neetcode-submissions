class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0 
        
        for unique in uniques:
            if (unique-1) not in uniques:
                length = 1
                while (unique + length) in uniques:
                    length += 1
                longest = max(length, longest)

        return longest
