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

        print(bucket)
       
        values = list(bucket.values())
        for value in values:
            
            if k == 0:
                break

            if len(value) != 0:
                result.append(value[0])
                k -= 1
            
        return result