from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i, num in enumerate(nums):
            target = 0-nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    result.add(tuple([nums[i], nums[j], nums[k]]))
                    break
        return list(result)