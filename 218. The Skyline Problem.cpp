#include <vector>
#include <set>
#include <map>
#include <iostream>
using namespace std;


class Solution {
public:
    vector<vector<int>> buildings;
    vector<vector<int>> result{};
    map<int, int, std::greater<int>> heightMap{};

    int getNextHeight(int x) {
        while (!heightMap.empty() && heightMap.begin()->second <= x)
        {
            heightMap.erase(heightMap.begin());
        }
        if (heightMap.empty())
        {
            return 0;
        }
        return heightMap.begin()->first;
    }

    void appendResult(int x, int height) {
        if (result.empty() || result.back()[1] != height && result.back()[0] != x)
        {
            result.push_back({x, height});
            return;
        }
        if (result.back()[0] == x)
        {
            int oldHeight = result.back()[1];
            result.pop_back();
            appendResult(x,max(oldHeight, height));
            return;
        }
    }

    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        this->buildings = buildings;

        buildings.push_back({INT32_MAX, INT32_MAX, -1});
        int currHeight = 0, currX = 0, nextX, height, x;

        for (auto &&building : buildings)
        {
            nextX = building[0];
            while (!heightMap.empty() && heightMap.begin()->second <= nextX)
            {
                height = heightMap.begin()->first;
                x = heightMap.begin()->second;
                auto erased = heightMap.erase(heightMap.begin());
                    if (x < currX)
                {
                    continue;
                }
                if (height == currHeight)
                {
                    currX = x;
                    currHeight = getNextHeight(currX);
                    appendResult(currX, currHeight);
                    continue;
                }
            }

            auto pair = heightMap.insert({building[2], building[1]});
            if (!pair.second)
            {
                pair.first->second = max(pair.first->second, building[1]);
            }
            if (currHeight < building[2])
            {
                currHeight = building[2];
                currX = building[0];
                appendResult(currX, currHeight);
            }
        }
        if (result.back()[1] != 0)
        {
            result.pop_back();
        }
        return result;
    }
};

int main()
{
    vector<vector<int>> arr{{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}};
    auto res = (new Solution())->getSkyline(arr);
}