from xml.etree.ElementTree import iselement


def is_eq(a: str, b: str):
    return a == '.' or a == b
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        patterns = []
        idx = 0

        # break the patterns
        for i in range(1, len(p)):
            if p[i] == '*':
                patterns.append(p[i-1:i+1])
            elif p[i-1] != '*': 
                patterns.append(f"{p[i-1]} ")
        if p[-1] != '*':
            patterns.append(f"{p[-1]} ")

        ls = len(s)
        lp = len(patterns)
        # setup grid
        grid = [[False] * (ls+1) for _ in range(lp + 1)]
        grid[0][0] = True
        
        for i in range(lp):
            for j in range(ls + 1):
                if grid[i][j]:
                    p = patterns[i]
                    if p[1] == ' ':
                        if j < ls and is_eq(p[0], s[j]):
                            grid[i + 1][j + 1] = True
                    else:
                        grid[i+1][j] = True
                        for k in range(1, ls - j + 1):
                            if is_eq(p[0], s[j + k - 1]):
                                grid[i+1][j + k] = True
                            else:
                                break
        
        return grid[-1][-1]


        print(p, patterns)

ss = [
    # ('aa', 'a'),
    # ('aa', 'a*'),
    # ('abcde', '.*'),
    # ('abcde', 'a.*c'),
    ('ccb', 'a*c*a*b')
]
for s in ss:
    sol = Solution()
    res = sol.isMatch(*s)
    print(s, res, sep='\n')

