class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [ [] for i in range(len(nums) + 1)]

        counts = {}

        #count the frequency of all numbers
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, cts in counts.items():
            frequencies[cts].append(num) # for all frequencies, add the number 

        output = []
        for i in range(len(frequencies) -1, 0, -1): # going backwards (since we want TOP K frequencies)
            for num in frequencies[i]: # iterate over the collection
                output.append(num)

                if len(output) == k:
                    return output
