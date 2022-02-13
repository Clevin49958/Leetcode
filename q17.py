from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_ = {
            '2': "abc",
            "3": 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        out = []
        n = len(digits)
        def get_s(idx: int, s:str):
            if idx == n:
                out.append(s)
            else:
                for c in dict_[digits[idx]]:
                    get_s(idx + 1, s + c)
        get_s(0, '')
        return out if len(out) > 1 else []

ins = [
    "",
    "23",
    "234",
    "2"
]

sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.letterCombinations(v)
    print(res)