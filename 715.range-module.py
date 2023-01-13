#
# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#

# @lc code=start
from bisect import bisect_left, bisect_right


class RangeModule:

    def __init__(self):
        self.starts = []
        self.ends = []

    def pretty(self) -> None:
        return list(zip(self.starts, self.ends))

    def addRange(self, left: int, right: int) -> None:
        # overlapping or touching :left >= end_a; start_b <= right
        after_index = bisect_left(self.ends, left)
        before_index = bisect_right(self.starts, right)
        if before_index > after_index:
            left = min(left, self.starts[after_index])
            right = max(right, self.ends[before_index - 1])
        self.starts = [*self.starts[:after_index], left, *self.starts[before_index:]]
        self.ends = [*self.ends[:after_index], right, *self.ends[before_index:]]

    def queryRange(self, left: int, right: int) -> bool:
        # contained: start_a <= left; right <= end_a
        after_index = bisect_right(self.starts, left)
        before_index = bisect_left(self.ends, right)
        return after_index - 1 == before_index

    def removeRange(self, left: int, right: int) -> None:
        after_index = bisect_left(self.ends, left)
        before_index = bisect_right(self.starts, right)
        reduced_left, reduced_right = left, right
        if before_index > after_index:
            reduced_left = min(left, self.starts[after_index])
            reduced_right = max(right, self.ends[before_index - 1])
        
        if left > reduced_left:
            if right < reduced_right:
                self.starts = [*self.starts[:after_index], reduced_left, right,         *self.starts[before_index:]]
                self.ends =   [*self.ends[:after_index],   left,         reduced_right, *self.ends[before_index:]]
            else:
                self.starts = [*self.starts[:after_index], reduced_left,                *self.starts[before_index:]]
                self.ends =   [*self.ends[:after_index],   left,                        *self.ends[before_index:]]
        elif right < reduced_right:
            self.starts =     [*self.starts[:after_index],               right,         *self.starts[before_index:]]
            self.ends =       [*self.ends[:after_index],                 reduced_right, *self.ends[before_index:]]
        else:
            self.starts =     [*self.starts[:after_index],                              *self.starts[before_index:]]
            self.ends =       [*self.ends[:after_index],                                *self.ends[before_index:]]

        

# @lc code=end

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
for ranges in ([1,3], [20, 30], [14, 16], [10, 14], [13, 15], [15, 17], [9, 10], [17,18]):
    print(obj.queryRange(*ranges))
    obj.addRange(*ranges)
    print(obj.pretty())

for ranges in ([9, 12], [15,18], [9, 18], [2, 10], [0, 40]):
    print(obj.queryRange(*ranges))

for ranges in ([4,5], [1,3], [2, 10], [12, 13], [16, 20], [0, 20]):
    obj.removeRange(*ranges)
    print(obj.pretty())


