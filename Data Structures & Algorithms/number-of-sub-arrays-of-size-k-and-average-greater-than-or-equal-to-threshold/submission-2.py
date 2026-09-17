class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        window = list()
        avg = 0
        res = 0
        total = 0


        for r in range(0, len(arr)):
            window.append(arr[r])
            if r - l + 1 == k:
                total = sum(window)
                avg = total / k
                if avg >= threshold:
                    res += 1
                total = total - arr[l]
                window.pop(0)
                avg = 0
                l += 1
            

        return res