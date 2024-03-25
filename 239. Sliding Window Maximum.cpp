#include <vector>
#include <queue>
using namespace std;

struct Node {
    int value;
    int index;
    bool is_valid = true;
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result(nums.size() - k + 1);
        vector<shared_ptr<Node>> pointers(nums.size());
        auto comp = [](shared_ptr<Node>& lhs, shared_ptr<Node>& rhs){return lhs->value < rhs->value;};
        priority_queue<shared_ptr<Node>, vector<shared_ptr<Node>>, decltype( comp )> pq(comp);

        for (size_t i = 0; i < k - 1; i++)
        {
            auto node = make_shared<Node>();
            node->value = nums[i];
            node->index = i;
            pq.push(node);
            pointers[i] = node;
        }
        for (size_t i = k - 1; i < nums.size(); i++)
        {
            auto node = make_shared<Node>();
            node->value = nums[i];
            node->index = i;
            pq.push(node);
            pointers[i] = node;
            auto top = pq.top();
            while (!top->is_valid)
            {
                pq.pop();
                top = pq.top();
            }
            result[i - k + 1] = top->value;
            pointers[i - k + 1]->is_valid = false;
        }
        
        return result;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    auto result = s.maxSlidingWindow(nums, k);
    return 0;
}