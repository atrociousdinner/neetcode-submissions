class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = 0
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        print(leftMax)

        rightMax[n-1] = 0
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        print(rightMax)

        res = 0

        for i in range(n):
            if min(leftMax[i], rightMax[i]) - height[i] < 0:
                continue
            else:
                res += min(leftMax[i], rightMax[i]) - height[i]
        return res
        