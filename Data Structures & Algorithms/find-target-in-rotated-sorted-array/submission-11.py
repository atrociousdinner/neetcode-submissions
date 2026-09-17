class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                #left sorted portion
                l = m + 1
            else:
                #right sorted portion
                r = m

        pivot = l

        def binary_search(left, right):

            while left <= right:
                m = left + (right - left)//2

                if nums[m] > target:
                    right = m - 1
                elif nums[m] < target:
                    left = m + 1
                else:
                    return m
            return -1
        
        result = binary_search(0, pivot-1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums)-1)
            


       