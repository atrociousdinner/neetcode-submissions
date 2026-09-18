from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, num in enumerate(nums):

            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            target = -num
            l = i + 1
            r = len(nums)-1
            summ = 0

            while l < r:
                summ = nums[l] + nums[r]
                if(summ) < target:
                    l += 1
                elif (summ) > target:
                    r -= 1
                else:
                    #we've found the triplet
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1

        return res