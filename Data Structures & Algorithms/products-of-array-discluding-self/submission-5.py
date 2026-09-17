class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre = 1
        pro = 1

        pre_list = []
        pro_list = []

        res = []

        pro_list = [0] * len(nums)

        for num in nums:
            pre = pre*num
            pre_list.append(pre)

        for i in range(len(nums)-1, -1, -1):
            pro = pro*nums[i]
            pro_list[i] = pro

        for i, num in enumerate(nums):
            left = pre_list[i-1] if i > 0 else 1
            right = pro_list[i+1] if i < len(nums)-1 else 1

            res.append(left*right)

        return res

            


        

