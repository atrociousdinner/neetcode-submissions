class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pro = 1
        zero_count = 0
        for num in nums:
            if num:
                pro *= num
            else:
                zero_count +=1
        
        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)

        for i, c in enumerate(nums):
            if zero_count:
                res[i] = 0 if c else pro
            else:
                res[i] = int(pro/c)
        return res

            


        

