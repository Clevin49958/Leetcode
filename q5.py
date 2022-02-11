class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s[0]
        if n == 2:
            return s if s[0] == s[1] else s[0]

        idx = 0
        max_l = 1
        max_s = s[0]
        while idx < n - 1:
            offsets = []
            if s[idx] == s[idx + 1]:
                offsets.append(1)
            if idx > 0 and s[idx - 1] == s[idx + 1]:
                offsets.append(0)
            for offset in offsets:
                start = idx
                end = idx + offset
                while start >= 0 and end < n and s[start] == s[end]:
                    start -= 1
                    end += 1
                d = end - start - 1
                if d > max_l:
                    max_l = d
                    max_s = s[start+1:end]
            idx += 1
        return max_s
s = "ccc"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)