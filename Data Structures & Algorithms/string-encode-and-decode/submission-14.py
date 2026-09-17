from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Format: <length>#<string>
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # read length until '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # substring after '#'
            word = s[j+1 : j+1+length]
            result.append(word)
            # move i pointer
            i = j + 1 + length
        return result
