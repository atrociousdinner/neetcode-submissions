class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index_hashmap = {}

        for i, num in enumerate(numbers):
            index_hashmap[num] = i+1
        
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in numbers:
                return ([index_hashmap[num], index_hashmap[diff]])
        