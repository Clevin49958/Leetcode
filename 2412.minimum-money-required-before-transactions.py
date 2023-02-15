#
# @lc app=leetcode id=2412 lang=python3
#
# [2412] Minimum Money Required Before Transactions
#

# @lc code=start
from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total = 0
        for i in range(len(transactions)):
            cost, cashback = transactions[i]
            transactions[i] = [cashback - cost, cost]
            if cashback - cost < 0:
                total += cost - cashback
        print(total)
        min_req = total
        for req, cost in transactions:
            if req > 0:
                min_req = max(min_req, total + cost)
            else:
                min_req = max(min_req, total + req + cost)
        return min_req
# @lc code=end

from util import test_local
test_local(
    Solution().minimumMoney,
    [[2,1],[5,0],[4,2]],
    [[3,0],[0,3]]
)