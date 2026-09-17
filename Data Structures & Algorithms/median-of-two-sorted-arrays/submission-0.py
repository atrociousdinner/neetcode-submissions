import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        arr = [0] * length

        i = 0 
        l = 0
        r = 0

        while (l < len(nums1) and r < len(nums2)):
            if nums1[l] < nums2[r]:
                arr[i] = nums1[l]
                l += 1
                i += 1
            else:
                arr[i] = nums2[r]
                r += 1
                i += 1
        
        while (l <len(nums1)):
            arr[i] = nums1[l]
            l += 1
            i += 1
        
        while (r <len(nums2)):
            arr[i] = nums2[r]
            r += 1
            i += 1

        return statistics.median(arr)



        