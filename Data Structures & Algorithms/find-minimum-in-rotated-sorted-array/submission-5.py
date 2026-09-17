class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l < r:
            m = l + (r-l)//2
            res = min(res, nums[m])

            if nums[m] > nums[l] and nums[m] < nums[r]:
                #Sorted portion
                return nums[l]

            elif nums[m] > nums[l] and nums[m] > nums[r]:
                #Left sorted portion
                res = min(res, nums[l])
                l = m + 1
            
            else:
                #Right sorted portion
                res = min(res, nums[r])
                r = m
        
        return res
