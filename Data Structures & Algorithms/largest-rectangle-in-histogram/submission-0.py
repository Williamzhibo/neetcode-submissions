class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, v in enumerate(heights):
            if not stack or v >= stack[-1][1]:
                stack.append((i,v)) #push a tuple onto our stack 
            else:
                maxArea = max(maxArea, v)
                index = i
                while stack and stack[-1][1] > v:
                    popped = stack.pop()
                    value = (i - popped[0]) * popped[1]
                    maxArea = max(value, maxArea)
                    index = popped[0]
                stack.append((index,v))
        while stack:
            popped = stack.pop()
            value = (len(heights) - popped[0]) * popped[1]
            maxArea = max(value, maxArea)
        return maxArea