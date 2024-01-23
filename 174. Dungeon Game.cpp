#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int calculateMinimumHP(vector<vector<int>> &dungeon)
    {
        vector<vector<int>> dp(dungeon.size(), vector<int>(dungeon[0].size(), INT_MAX));
        int m = dungeon.size();
        int n = dungeon[0].size();
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1]);

        for (int i = m - 1; i >= 0; i--)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (i != m - 1 && dp[i + 1][j] != INT_MAX)
                {
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] - dungeon[i][j] > 0 ? dp[i + 1][j] - dungeon[i][j] : 1);
                }
                if (j != n - 1 && dp[i][j + 1] != INT_MAX)
                {
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] - dungeon[i][j] > 0 ? dp[i][j + 1] - dungeon[i][j] : 1);
                }
            }
        }
        return dp[0][0];
    }
};

int main()
{
    vector<vector<int>> dungeon = {{2}, {1}};
    cout << Solution().calculateMinimumHP(dungeon);
    return 0;
}