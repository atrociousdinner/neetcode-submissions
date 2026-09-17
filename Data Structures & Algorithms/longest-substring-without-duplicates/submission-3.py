class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        length = 0
        max_length = 0
        l = 0

        for r, char in enumerate(s):
            while char in window:
                max_length = max(length, max_length)
                length = 0
                window.remove(s[l])
                l += 1
            length += 1
            window.add(s[r])
            print(window)
        
        return max_length