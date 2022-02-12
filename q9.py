from math import log10
from math import ceil, floor


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        n_digits_supposed = floor(log10(x)) + 1
        while x >= 10 or n_digits_supposed > 1 and x > 0:
            n = floor(log10(x)) + 1
            if n < n_digits_supposed:
                start = 0
            else:
                start = x // (10 ** (n - 1))
            end = x % 10
            if start != end:
                return False
            if n < n_digits_supposed:
                x //=10
            else:
                x = x % (10 ** (n-1)) // 10
            n_digits_supposed -= 2
            pass
        return True
        

ss = [11, 1001, 120021, 120010021, 120001021, 10011001]
for s in ss:
    sol = Solution()
    res = sol.isPalindrome(s)
    print(res)

