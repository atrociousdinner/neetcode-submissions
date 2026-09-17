class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_i = height[i]
        max_j = height[j]
        sum_height = 0
        while i < j:
            if max_i < max_j:
                i+=1
                max_i = max(max_i, height[i])
                sum_height += max_i - height[i]
            
            else:
                j -= 1
                max_j = max(max_j, height[j])
                sum_height += max_j - height[j]
        return sum_height
        