from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
       #Format: "<length>#"
       res2 = []
    #    for st in strs:
    #        res2.append(f"{len(st)}:{st}")
    #    print(res2)
    #    res2 = ''.join(res2)
    # #    print(res2)

       return (''.join(f"{len(st)}:{st}" for st in strs))

    def decode(self, s: str) -> List[str]:
        i = 0
        res =[]

        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
