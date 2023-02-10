#
# @lc app=leetcode id=1687 lang=python3
#
# [1687] Delivering Boxes from Storage to Ports
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        boxes.insert(0, (-1,0))
        n = len(boxes)
        dp = [defaultdict(tuple) for _ in range(len(boxes))]
        dp[0][0]= (0, 0)

        # perf = 0
        for i, box in list(enumerate(boxes))[1:]:
            nboxes = 1
            total_weight = boxes[i][1]
            trips = 0
            arrive_at = box[0]
            for j in range(i-1, -1, -1):
                extra_trip = 0 if boxes[j][0] == arrive_at else 1
                for key, value in dp[j].items():
                    if value[0] >= nboxes and value[1] >= total_weight:
                        dp[i][key + trips + extra_trip] = max(dp[i][key + trips + extra_trip], (value[0] - nboxes, value[1] - total_weight))
                    elif maxBoxes >= nboxes and maxWeight >= total_weight:
                        dp[i][key + trips + (2 if j != 0 else 1)] = max(dp[i][key + trips + (2 if j != 0 else 1)], (maxBoxes - nboxes, maxWeight - total_weight))
                    else:
                        break
                trips += extra_trip
                arrive_at = boxes[j][0]
                nboxes += 1
                total_weight += boxes[j][1]
                # perf += 1
                # reduce lookback to be almost O(1)
                if boxes[j][0] != boxes[j + 1][0]:
                    break
                if maxBoxes < nboxes or maxWeight < total_weight:
                    break

            # reduce redundent info
            if i < n - 1 and box[0] != boxes[i + 1][0] and len(dp[i]) > 1:
                min_key = min(dp[i].keys())
                dp[i] = {min_key: dp[i][min_key]}
            
            # print(i, perf, dp[i])
        return min(dp[-1].keys()) + 1

        
# @lc code=end
import util
util.test_local(
    Solution().boxDelivering,
    ([[1,1],[2,1],[1,1]], 2, 3, 3),
    ([[1,2],[3,3],[3,1],[3,1],[2,4]], 3,3,6),
    ([[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], 3, 6, 7),
    expand=True
)