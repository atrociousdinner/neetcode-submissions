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
        for i, char in enumerate(s):
            if char == '#':
                j = i+1
                length = int(s[i-1])
                i = j + length
                res.append(s[j:i]) 
        return res
       

