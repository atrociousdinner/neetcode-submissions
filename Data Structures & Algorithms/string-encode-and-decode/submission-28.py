from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f'{len(word)}#{word}')
        res = ''.join(res)
        print(res)
        return res



       
    def decode(self, s: str) -> List[str]:
        length = 0
        word = ''
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            word = s[j+1: j+length+1]
            res.append(word)

            i = j+length+1

        return res

