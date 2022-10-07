#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start
import bisect

class MyCalendarThree:
    def calc(self, start, end):
        maxk = 0
        k = 0
        i = 0
        j = 0
        n = len(start)
        while i < n and j < n:
            if i < n and start[i] < end[j]:
                i += 1
                k += 1
                if k > maxk:
                    maxk = k
            elif j < n and (i == n or start[i] >= end[j]):
                j += 1
                k -= 1
        return maxk
    def __init__(self):
        self.starts = []
        self.ends = []
    def book(self, start: int, end: int) -> int:
        bisect.insort(self.starts, start)
        bisect.insort(self.ends, end)
        return self.calc(self.starts, self.ends)
        pass
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end

myCalendarThree = MyCalendarThree()
print(myCalendarThree.book(10, 20)) # return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
print(myCalendarThree.book(50, 60)) # return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
print(myCalendarThree.book(10, 40)) # return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
print(myCalendarThree.book(5, 15)) # return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
print(myCalendarThree.book(5, 10)) # return 3
print(myCalendarThree.book(25, 55)) # return 3