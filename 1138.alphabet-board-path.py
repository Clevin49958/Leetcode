#
# @lc app=leetcode id=1138 lang=python3
#
# [1138] Alphabet Board Path
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        get_pos = lambda chr: ord(chr) - 97

        commands = []
        curr = 0
        for chr in target:
            pos = get_pos(chr)
            dy = pos // 5 - curr // 5
            dx = pos % 5 - curr % 5
            if dy > 0:
                commands.append(('R' if dx > 0 else 'L') * abs(dx))
                commands.append('D' * dy)
            else:
                commands.append('U' * abs(dy))
                commands.append(('R' if dx > 0 else 'L') * abs(dx))
            
            commands.append('!')
            curr = pos
        return ''.join(commands)

# @lc code=end

from util import test_local
test_local(Solution().alphabetBoardPath, "leet", "code", "xzx")