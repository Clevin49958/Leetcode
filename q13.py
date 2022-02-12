class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        last = 100000
        idx = 0
        out = 0
        while idx < len(s):
            v = symbols[s[idx]]
            if v > last:
                out -= last * 2
            out += v
            last = v
            idx += 1
        return out


ins = [
    'III',
    'LVIII',
    'MCMXCIV',
    'CDXLIV',
]

for v in ins:
    sol = Solution()
    res = sol.romanToInt(v)
    print(res)
