class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i

        print(hashmap)

        for i, num in enumerate(nums):
            y = target - num
            print(y)
            if y in hashmap and hashmap[y] != i:
                return [i, hashmap[y]]

            


        