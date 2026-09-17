class Solution:

    def encode(self, strs: List[str]) -> str:
        string2 = ','.join(strs)
        # print(string2)
        # self.decode(string2 + ',')
        return string2+','

    def decode(self, s: str) -> List[str]:
        result = []
        word = ''

        # if len(s) == 1:
        #     return result

        for i, char in enumerate(s):
            if char == ',':
                result.append(word)
                word=''
            else:
                word += char
        return result


