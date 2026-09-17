class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #Maps each element with its frequency
        bucket = {}
        result = []
        for num in nums:
            hashmap[num] =  1 + hashmap.get(num, 0)
        
        for i in range(len(nums), 0, -1):
            bucket[i] = []

        for key, value in hashmap.items():
            if value in bucket:
                bucket[value].append(key)

        keys = list(bucket.keys())
        values = list(bucket.values())

        for i in range(len(bucket)):

            if k == 0:
                break

            if len(values[i]) != 0:
                k -= 1
                result.append(values[i][0])

        return result