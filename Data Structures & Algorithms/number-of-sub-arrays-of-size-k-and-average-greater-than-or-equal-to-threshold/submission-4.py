class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        window = list()
        res = 0
        total = 0

        for r in range(len(arr)):
            window.append(arr[r])
            if r - l + 1 == k:
                total = sum(window)
                if (total/k) >= threshold:
                    res += 1
                total -= arr[l]
                window.pop(0)
                l += 1
            

        return res