class Solution:

    def encode(self, strs: List[str]) -> str:
        string2 = '#'.join(strs)
        
        if not strs:
            return ""
        return string2+'#'

    def decode(self, s: str) -> List[str]:
        result = []
        word = ''
        print(s)
        for char in s:
            if char == '#':
                result.append(word)
                word = ''
            else:
                word += char
        return result


