class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        result = []
        post = [0] * len(nums)

        pre_pro = 1
        post_pro = 1

        for num in nums:
            pre_pro *= num
            pre.append(pre_pro)
        
        for i in range(len(nums)-1, -1, -1):
            post_pro *= nums[i]
            post[i] = post_pro

        for i, num in enumerate(nums):
            if i == 0:
                result.append(1*post[i+1])
            elif i == len(nums)-1:
                result.append(pre[i-1]*1)
            else:
                result.append(pre[i-1]*post[i+1])

        return(result)
        

            


        

