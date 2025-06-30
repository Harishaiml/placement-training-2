from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        values = self.store[key]
        i = bisect.bisect(values, (timestamp, chr(127)))
        return values[i-1][1] if i else ""
