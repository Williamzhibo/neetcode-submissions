class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #ok so for this, two pointer, want to maximize total area by holding a sum. every delta inwards -> requires new increase to be prev max height more (since we lose a slice of width)


        biggest = 0

        l, r = 0, len(heights) - 1

        while l < r: 
            height = min(heights[l], heights[r])
            biggest = max(height * (r - l), biggest) #volume is higher bounder * width 
            if heights[l] > heights[r]: #left side is bigger bounder (right is limiting gain)
                r -= 1
            else: 
                l += 1
        return biggest
