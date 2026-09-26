class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for i in range(len(nums), 0, -1):
            bucket[i] = []

        for key, value in hashmap.items():
            if value in bucket:
                bucket[value].append(key)

        values = list(bucket.values())
        # print(values)

        res = []
        for value in values:
            for num in value:
                res.append(num)
                k -= 1

                if k == 0:
                    return res