class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash[key]

        l = 0
        r = len(values)-1
        res = ""

        while l <= r:
            m = l + (r-l)//2

            if values[m][1] < timestamp:
                l = m + 1
                res = values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else: return values[m][0]
        return res
