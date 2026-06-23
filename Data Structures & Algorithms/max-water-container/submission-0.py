class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest,left, right = 0,0,len(heights) - 1

        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            if (volume > greatest):
                greatest = volume
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return greatest