class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        s = s.lower()

        result = ''.join(c.lower() for c in s if c.isalnum())

        i = 0
        j = len(result) - 1

        while i <= j:
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1

        return True

        