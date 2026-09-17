class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #Maps each element with its frequency
        result = []
        for num in nums:
            hashmap[num] =  1 + hashmap.get(num, 0)

        hashmap = sorted(hashmap.items(), key = lambda x:x[1], reverse = True)
        print(hashmap)
        for i in range(0, k):
            result.append(hashmap[i][0])
        return result