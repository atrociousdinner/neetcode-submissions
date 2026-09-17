class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # Mapping character count to the string
        for string in strs:
            count = [0] * 25
            for char in string:
                count[ord(char) - ord('a')] += 1
            hashMap[tuple(count)].append(string)
        return list(hashMap.values())
