class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i, temp in enumerate(temperatures):
            found = False
            for j in range(i+1, len(temperatures)):
                if temp < temperatures[j]:
                    distance = j - i
                    result.append(distance)
                    found = True
                    break
            if not(found):
                result.append(0)
        
        return(result)
