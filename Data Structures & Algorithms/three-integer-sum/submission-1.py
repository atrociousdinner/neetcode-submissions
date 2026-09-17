from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
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
                    if[nums[i], nums[j], nums[k]] in result:
                        continue
                    else:
                        result.append([nums[i],nums[j],nums[k]])
                    break
        return result