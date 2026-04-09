class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value, timestamp))
        else:
            self.timeMap[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        entries = self.timeMap.get(key, [])
        l, r = 0, len(entries) - 1
        res = ""

        while l <= r:
            m = (r-l)//2+l
            if entries[m][1] <= timestamp:
                res = entries[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        
