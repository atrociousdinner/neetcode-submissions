class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #Maps each element with its frequency
        result = []
        for num in nums:
            hashmap[num] =  1 + hashmap.get(num, 0)

        for key, value in hashmap.items():
            if value >= k:
                result.append(key)
        return result