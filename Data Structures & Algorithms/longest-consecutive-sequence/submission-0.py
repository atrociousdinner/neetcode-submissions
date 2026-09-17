class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(list) # Mapping the largest integer in a sequence with the sequence
        nums = sorted(nums)
        for num in nums:
            
            if num in hashmap:
                continue

            if num-1 in hashmap:
                hashmap[num] = hashmap.pop(num-1)

            hashmap[num].append(num)
        print(list(hashmap.values()))
        result = []
        values = list(hashmap.values())
        for value in values:
            result.append(len(value))

        return (max(result))
