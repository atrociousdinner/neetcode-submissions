class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash[key]
        timestamps = [value[1] for value in values]
        
        l = 0
        r = len(timestamps) - 1
        res = ""

        while l <= r:
            m = l + (r-l)//2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        
