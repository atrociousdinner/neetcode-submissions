class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        length = 0
        l = 0

        if len(s) == 1:
            return 1

        for r, char in enumerate(s):
            while char in window:
                length = max(length, r-l)
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            print(window)
        
        return length