#include <string>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Codec {
public:
    void serializeRecur(TreeNode* root, vector<string>& cache)
    {
        if (root == nullptr)
        {
            return;
        }
        cache.push_back(to_string(root->val));
        cache.push_back("(");
        serializeRecur(root->left, cache);
        cache.push_back("|");
        serializeRecur(root->right, cache);
        cache.push_back(")");
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        vector<string> cache;
        serializeRecur(root, cache);
        string result;
        for (auto& str : cache)
        {
            result += str;
        }
        return result;   
    }

    int parseNum(string& data, size_t& index)
    {
        int result = 0, sign=1;
        while (index < data.size() && data[index] != '(' && data[index] != ')' && data[index] != '|')
        {
            if (data[index] == '-')
            {
                sign = -1;
                index++;
                continue;
            }
            result = result * 10 + data[index] - '0';
            index++;
        }
        return result * sign;
    }
    TreeNode* deserialiseRecur(string& data, size_t& index)
    {
        if (index >= data.size())
        {
            return nullptr;
        }
        TreeNode* root = new TreeNode(parseNum(data, index));
        index++;
        if (data[index] != '|')
        {
            root->left = deserialiseRecur(data, index);
        }
        index++;
        if (data[index] != ')')
        {
            root->right = deserialiseRecur(data, index);
        }
        index++;
        return root;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        size_t index = 0;
        return deserialiseRecur(data, index);
    }
};

int main()
{
    Codec c;
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(-7);
    root->right = new TreeNode(-3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);
    string serialized = c.serialize(root);
    TreeNode* deserialized = c.deserialize(serialized);
    return 0;
}