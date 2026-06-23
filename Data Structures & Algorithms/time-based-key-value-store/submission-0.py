import bisect
from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.timeMap[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.timeMap[key]

        l = 0
        r = len(lst) - 1
        res = ""
        #this is just a sorting/finding algorithm finding timestamp, returning left if not 
        while l <= r:
            mid = (l + r) // 2
            
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            
            if lst[mid][0] <= timestamp:
                res = lst[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)