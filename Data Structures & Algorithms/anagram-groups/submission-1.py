class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # Mapping bit string to the words
        for i in range(0, len(strs)):
            count = [0] * 25
            for char in strs[i]:
                count[ord(char) - ord ("a")] += 1
            hashmap[tuple(count)].append(strs[i])
        return list(hashmap.values())
