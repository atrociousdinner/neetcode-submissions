class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(list) #Mapping teh largest integer of a sequence to the sequence
        nums = sorted(nums)
        max_length = 0

        for num in nums:

            if num in hashmap:
                continue
            
            if num-1 in hashmap:
                hashmap[num] = hashmap.pop(num-1)

            hashmap[num].append(num)

        # print(list(hashmap.values()))
        sub_lists = list(hashmap.values())

        for sub in sub_lists:
            max_length = max(len(sub), max_length)

        return max_length
