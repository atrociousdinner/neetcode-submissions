class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(start_index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                stackI, stackH = stack.pop()
                area = stackH * (i - stackI)
                maxArea = max(area, maxArea)
                start = stackI
            stack.append((start, h))

        for start, height in stack:
            area = height * (len(heights) - start)
            maxArea = max(area, maxArea)

        return maxArea