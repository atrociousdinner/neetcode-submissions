class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i, num in enumerate(nums):
            pro = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    pro *= nums[j]
            result.append(pro)
        
        return result

