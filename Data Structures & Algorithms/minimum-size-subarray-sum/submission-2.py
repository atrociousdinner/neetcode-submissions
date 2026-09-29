class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        length = float("inf")

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                length = min(length, r-l+1)
                summ -= nums[l]
                l += 1

        return 0 if length == float("inf") else length
            