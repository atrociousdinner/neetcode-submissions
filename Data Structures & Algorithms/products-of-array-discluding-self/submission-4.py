class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre = 1

        for i, num in enumerate(nums):
            result.append(pre)
            pre = pre * num
        
        pos = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * pos
            pos = pos * nums[i]
        
        return result

            


        

