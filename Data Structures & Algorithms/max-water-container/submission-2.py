class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        area = 0
        max_area = area

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(area, max_area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
