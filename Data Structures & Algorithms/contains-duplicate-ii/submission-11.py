class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l = 0

        for r in range(0, len(nums)):
            if r - l + 1 > k + 1:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True
            
            window.add(nums[r])

        return False