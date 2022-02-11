# could have just zigzag and store the empty sections in the same column
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr_empty = [None] * numRows
        col_count = 0
        n = len(s)
        idx = 0
        full = []
        pattern = 0
        while idx < n:
            if pattern == 0 or numRows <= 2:
                end = min((idx + numRows, n))
                arr = arr_empty.copy()
                for i in range(end-idx):
                    arr[i] = s[i + idx]
                full.append(arr)
                pattern = 1 - pattern
            else:
                end = min((idx + numRows - 2, n))
                for i in range(end-idx):
                    arr = arr_empty.copy()
                    arr[numRows - i - 2] = s[i + idx]
                    full.append(arr)
                pattern = 1 - pattern
            idx = end
            end = min((idx + numRows, n))
        
        # print(full)
        res = ""
        # export
        for item in zip(*full):
            # print(item)
            res += ''.join(filter(None, item))
        return res
s = "AB"
sol = Solution()
res = sol.convert(s, 1)
print(res)