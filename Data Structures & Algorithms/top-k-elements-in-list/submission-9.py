class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = {}

        #frequency hashmap
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        

        #bucket
        for i in range(len(nums), 0, -1):
            bucket[i] = [] #Initialize each count to empty lists initially

        for key, value in hashmap.items():
            if value in bucket:
                bucket[value].append(key)

        values = list(bucket.values())
        res = []

        for value in values:

            if k == 0:
                break

            if len(value) != 0:
                for num in value:
                    res.append(num)
                    k -= 1
        
        return res
