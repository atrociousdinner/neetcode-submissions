class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        result = []
        post = [0] * len(nums)

        pre_pro = 1
        post_pro = 1
        pro = 1

        for i, num in enumerate(nums):
            if i == 0:
                result.append(pro)
                continue
            pro *= nums[i-1]
            result.append(pro)

        print(result)

        pro = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            pro *= nums[i+1]
            result[i] = result[i] * pro

        return(result)
        

            


        

