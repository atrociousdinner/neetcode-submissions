class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = ''

        for char in s:
            if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')) or (ord(char) >= ord('0') and ord(char) <= ord('9')):
                result+= char.lower()
        
        i =0
        j = len(result)-1

        while i < j:
            if result[i] != result[j]:
                print(f"i: ${result[i]}   |||  j:${result[j]}")
                return False
            j -= 1
            i += 1
        return True
        