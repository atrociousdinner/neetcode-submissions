class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashset = {}
        maxf = 0

        for r in range (len(s)) :
            hashset[s[r]]=1+ hashset.get(s[r], 0)
            maxf = max(maxf, hashset[s[r]])
            while (r-l+1) - maxf > k:
                hashset[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
