#include <vector>
#include <set>
#include <map>
using namespace std;


class Solution {
public:
    int valueDiff;
    bool matches(multiset<int> &cache, multiset<int>::iterator it){
        int value = *it;
        if (it != cache.begin())
        {
            it--;
            if (abs(*it - value) <= valueDiff)
            {
                return true;
            }
            it++;
        }
        if (++it != cache.end())
        {
            if (abs(*it - value) <= valueDiff)
            {
                return true;
            }
        }
        return false;
    }
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        indexDiff = min(indexDiff, (int)nums.size()-1);
        this->valueDiff = valueDiff;
        multiset<int> curr{};
        for (size_t i = 0; i <= indexDiff; i++)
        {
            auto it = curr.insert(nums[i]);
            if (matches(curr, it))
            {
                return true;
            }
        }


        for (size_t i = indexDiff+1; i < nums.size(); i++)
        {
            curr.erase(curr.find(nums[i-indexDiff-1]));
            auto it = curr.insert(nums[i]);
            if (matches(curr, it))
            {
                return true;
            }
        }
        return false;
    }
};

int main(){
    vector<int> arr{1,3,6,4};
    (new Solution())->containsNearbyAlmostDuplicate(arr, 3,1);
}