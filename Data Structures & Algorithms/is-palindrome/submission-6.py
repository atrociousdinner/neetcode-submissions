class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        s = s.lower()

        for char in s:
            if((ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('0') and ord(char) <= ord('9'))):
                result += char.lower()
        
        i = 0
        j = len(result)-1

        while i < j:
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1
        return True
        