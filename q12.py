class Solution:
    def intToRoman(self, num: int) -> str:
        src = [
            ['I', 'V', 'X'],
            ['X', 'L','C'], 
            ['C', 'D', 'M'],
            ['M']
        ]
        lst = [
            [],
            [0],
            [0,0],
            [0,0,0],
            [0,1],
            [1],
            [1,0],
            [1,0,0],
            [1,0,0,0],
            [0,2]
        ]
        nums = []
        while num > 0:
            nums.append(num % 10)
            num //= 10
        n = len(nums)
        nums.reverse()
        nums = list(map(lambda dig:lst[dig], nums))
        # print(nums)
        for i in range(len(nums)):
            nums[i] = ''.join(map(lambda idx: src[n-i -1][idx], nums[i]))
        # print(nums)
        nums = ''.join(nums)
        # print(nums)
        return nums

ss = [3, 58, 1994 , 444]
for s in ss:
    sol = Solution()
    res = sol.intToRoman(s)
    print(res)

