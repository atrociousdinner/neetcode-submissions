class Solution:
    def isPalindrome(self, s: str) -> bool:
        i =0
        j = len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1
        return True
        