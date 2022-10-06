#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# @lc code=start
from collections import defaultdict
from typing import List


class TimeMap:
    def __init__(self):
        self.data = defaultdict(dict)
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value
        self.keys[key].append(timestamp)
        # print(self.data, self.keys)

    def bs_lower(self, arr: List[int], v: int, s, t):
        if v < arr[s]:
            return -1
        if s == t:

            return arr[s]
        mid = (s + t) // 2 + 1
        if arr[mid] > v:
            return self.bs_lower(arr, v, s, mid - 1)
        else:
            return self.bs_lower(arr, v, mid, t)

    def get(self, key: str, timestamp: int) -> str:
        # print(key, timestamp)
        if key not in self.keys:
            return ""
        t = self.bs_lower(self.keys[key], timestamp, 0, len(self.keys[key]) - 1)
        if t == -1:
            return ""
        else:
            return self.data[key][t]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

timeMap = TimeMap()
timeMap.set(
    "foo", "bar", 1
)  #  store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1)  #  return "bar"
timeMap.get(
    "foo", 3
)  #  return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set(
    "foo", "bar2", 4
)  #  store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4)  #  return "bar2"
timeMap.get("foo", 5)  #  return "bar2"
