class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = set()
        l = 0
        length = float("inf")
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                length = min(length, r-l+1)
                summ -= nums[l]
                l += 1


        return 0 if length == float("inf") else length