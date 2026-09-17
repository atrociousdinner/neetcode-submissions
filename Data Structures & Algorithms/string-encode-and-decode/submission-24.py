from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(f'{len(st)}#{st}')
        res = ''.join(res)
        return res



       
    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        i = 0
        while i != len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
       

