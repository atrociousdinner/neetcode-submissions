class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        total = 0

        for r in range(len(arr)):
            total += arr[r]
            if r - l + 1 == k:
                if(total/k) >= threshold:
                    res += 1
                total = total - arr[l]
                l += 1
        
        return res