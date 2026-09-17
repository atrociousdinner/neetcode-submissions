class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        
        area = 0
        greatest_area = area
        while i < j:
            area = ((j-i) * min(heights[i], heights[j]))
            if(area > greatest_area):
                greatest_area = area
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return greatest_area
