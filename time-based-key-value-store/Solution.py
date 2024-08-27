from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]

        if not data:
            return ''

        l = 0
        r = len(data) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if data[m][0] == timestamp:
                return data[m][1]
            elif data[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        return data[r][1] if data[r][0] < timestamp else ''
