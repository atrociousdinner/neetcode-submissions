class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for l in range(len(s)):
            count = {}
            maxf = 0
            for r in range(l, len(s)):
                count[s[r]] = 1 + count.get(s[r], 0)
                maxf = max(maxf, count[s[r]])
                if (r-l+1) - maxf <= k:
                    res = max(r-l+1,res)

        return res
