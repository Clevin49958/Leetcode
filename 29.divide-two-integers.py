#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def is_bigger(a:int, b:int)->bool:
            if a >= 0:
                return a >= b
            else:
                return a <= b
        if divisor == -2 ** 31:
            if dividend == divisor:
                return 1
            else:
                return 0
        pairs = []
        sign = -1 if ((divisor>0) ^ (dividend>=0)) else 1
        divisor //= sign
        q, idx, v = 0, divisor, sign
        print(sign, divisor, is_bigger(dividend, divisor))

        while is_bigger(dividend, idx):
            pairs.append((idx, v))
            idx *= 2
            v *= 2
        print(pairs)
        while pairs:
            idx, v = pairs.pop()
            if is_bigger(dividend, idx):
                dividend -= idx
                q += v
                if dividend == 0:
                    break
        if q >= 2 ** 31:
            return 2 ** 31 - 1
        elif q < -2 ** 31:
            return -2 ** 31
        else:
            return q
# @lc code=end

ins = [
    # (10, -3),
    # (-10, 3),
    # (-10, -3),
    # (7, -3),
    # (0, 1)
    # (-1, 1)
    (-2147483648, 2)
]

sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.divide(*v)
    print(res)