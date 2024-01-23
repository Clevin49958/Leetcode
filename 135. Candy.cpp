#include <vector>
#include <numeric>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        struct pair
        {
            int score;
            size_t index;
        };

        vector<pair> list ( ratings.size() );
        for (size_t i = 0; i < ratings.size(); i++)
        {
            list[i].score = ratings[i];
            list[i].index = i;
        }

        sort(list.begin(), list.end(), [](pair a, pair b) { return a.score < b.score; });
        
        vector<int> candies ( ratings.size() );

        for (auto &&pair : list)
        {
            const int index = pair.index;
            candies[index] = 1;
            if (index > 0 && ratings[index] > ratings[index - 1])
                candies[index] = max(candies[index], candies[index - 1] + 1);

            if (index < ratings.size() - 1 && ratings[index] > ratings[index + 1])
                candies[index] = max(candies[index], candies[index + 1] + 1);
        }
        
        return accumulate(candies.begin(), candies.end(), 0);
    }
};

int main()
{
    vector<int> ratings { 1,2,2 };
    cout << Solution().candy(ratings);
    return 0;
}