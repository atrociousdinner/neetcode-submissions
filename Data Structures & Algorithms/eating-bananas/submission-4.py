import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            m = (l+r) // 2
            hour = 0
            for pile in piles:
                hour = hour + math.ceil((pile/m)) 
            if hour <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k