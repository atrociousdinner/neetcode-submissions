class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = [value, timestamp]
        self.hashmap[key].append(values)

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        print(values)
        l = 0 
        r = len(values)-1
        res = ""
        while l <= r:
            m = l + (r-l)//2

            if values[m][1] > timestamp:
                r = m-1
            elif values[m][1] < timestamp:
                l = m+1
                res = values[m][0]
            else:
                return values[m][0]
        return res

