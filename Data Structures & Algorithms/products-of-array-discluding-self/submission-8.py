class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list = []
        pro_list = []
        res = []

        sing = 1
        pro_list = [0] * len(nums)

        for num in nums:
            sing = sing*num
            pre_list.append(sing)
        
        sing = 1

        for i in range(len(nums)-1, -1, -1):
            sing = sing * nums[i]
            pro_list[i] = sing

        # print(pre_list)
        # print(pro_list)

        for i, num in enumerate(nums):
            left = pre_list[i-1] if i != 0 else 1
            right = pro_list[i+1] if i != len(nums)-1 else 1

            res.append(left*right)

        return res

            


        

