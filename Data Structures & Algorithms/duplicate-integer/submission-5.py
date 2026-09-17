class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = [] 

        for num in nums:
            if num in map:
                return True
            map.append(num)
        return False