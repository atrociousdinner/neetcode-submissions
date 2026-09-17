class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''

        for char in s:
            if((ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))):
                result += char.lower()
        
        i = 0
        j = len(result)-1

        while i < j:
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1
        return True
        