class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.data.get(key, [])
        l, h = 0, len(pairs) -1
        res = ""

        while l <= h:
            mid = (l + h) // 2
            if pairs[mid][1] <= timestamp:
                res = pairs[mid][0]
                l = mid + 1
            else:
                h = mid - 1
        
        return res

