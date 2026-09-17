class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        avg = 0
        for i in range(0, len(arr)-k+1):
            summ = arr[i]
            for j in range(i+1, i+k):
                summ += arr[j]
            avg = summ/k
            print(avg)
            if avg >= threshold:
                res += 1
            avg = 0
            

        return res