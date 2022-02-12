from math import ceil, floor, log10


class Solution:
    def reverse(self, x: int) -> int:

        sign = 1 if x >= 0 else -1
        x = abs(x)
        threshold = 2 ** 31
        if sign == 1:
            threshold -= 1

        output = 0

        while x > 0:
            digit = x % 10
            output = digit + output * 10 
            x //= 10
            if output > threshold:
                return 0
            
            # print(output)

        return output * sign

s = 2147483647
sol = Solution()
res = sol.reverse(s)
print(res)