class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        n = len(s)
        letters = {}
        l = 0
        max_l = 0
        while end < n:
            if s[end] in letters:
                # remove anything up to existing copy of s[end]
                idx = letters[s[end]]
                for k, v in list(letters.items()):
                    if v < idx:
                        del letters[k]
                letters[s[end]] = end
                start = idx + 1
                l = end - idx
            else:
                letters[s[end]] = end
                l += 1
            if l > max_l:
                max_l = l
            end += 1
        return max_l

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))

