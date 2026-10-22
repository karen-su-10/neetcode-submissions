class TimeMap:

    def __init__(self):
     #O(n*m) space, key = key, value -- a sorted listed by timestamp each element =[val, timestamp]
     self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None: 
    #O(1)-- natually appending, increasd by timestamp
        if key not in self.m:
            self.m[key] = []
        self.m[key].append([value,timestamp])
       
    def get(self, key: str, timestamp: int) -> str:
    #O(logn)
        res, value = "", self.m.get(key,[])
        l, r = 0, len(value)-1
        while l<=r:
            m = (l+r)//2
            if value[m][1] <= timestamp:
                res = value[m][0]
                l =  m +1
            else:
                r = m-1
        return res
        
