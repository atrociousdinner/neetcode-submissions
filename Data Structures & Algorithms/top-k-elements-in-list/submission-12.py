class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = {}

        #hashmap
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        #bucket
        for i in range(len(nums), 0, -1):
            bucket[i] = []

        for key, value in hashmap.items():
            if value in bucket:
                bucket[value].append(key)

        values = list(bucket.values())

        res = []

        for value in values:
            if k == 0:
                break

            for num in value:
                res.append(num)
                k -= 1

        return res