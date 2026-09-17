class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]



        