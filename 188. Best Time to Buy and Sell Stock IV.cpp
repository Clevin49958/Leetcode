#include <vector>
#include <numeric>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        auto minimum = new int[n][1000]();
        for (size_t i = 0; i < n; i++)
        {
            int curr = prices[i];
            for (size_t j = i; j < n; j++)
            {
                curr = min(curr, prices[j]);
                minimum[i][j] = curr;
            }
        }
        
        int maxProfit = 0;
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 0));
        for (size_t l = 1; l < k + 1; l++) {
            for (size_t i = 1; i < n; i++)
            {
                int partial = 0, curr;
                for (size_t j = 0; j < i; j++)
                {
                    curr = dp[l-1][j] + prices[i] - minimum[j][i-1];
                    partial = max(partial, curr);
                }
                dp[l][i] = partial;
                maxProfit = max(maxProfit, partial);
                printf("%d ", dp[l][i]);
            }
            printf("\n");
        }
        return maxProfit;
        
    }
};

int main()
{
    vector<int> prices{3,2,6,5,0,3};
    cout << (new Solution())->maxProfit(2, prices);
}