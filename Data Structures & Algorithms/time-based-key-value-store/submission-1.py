class TimeMap:

    def __init__(self):
        self.dynamicdict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dynamicdict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.dynamicdict[key]
        l, r = 0, len(entries) - 1
        saved_val = ""
        while l <= r:
            mid = (l + r) // 2
            if entries[mid][1] <= timestamp:
                saved_val = entries[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return saved_val
        
