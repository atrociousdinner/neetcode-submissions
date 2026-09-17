class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        window = set()
        l = 0
        length = 0

        for r in range(len(s)):
            print('Iteraion No: ', r+1)
            while s[r] in window:
                print('Window looks like: ', window)
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = max(length, r-l+1)

        return length
