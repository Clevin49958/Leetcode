#include <string>
#include <vector>
using namespace std;


    struct Node {
        Node* children[26];
        bool isTerminal = false;
        bool isFound = false;
    };

class Trie {
public:

    Node* trie;

    Trie() {
        trie = new Node{nullptr};
    }
    
    void insert(string word) {
            Node* node = trie;
        for (auto const c: word) {
            int i = c-97;
            if (!node->children[i]){
                node->children[i] = new Node{nullptr};
            }
            node = node->children[i];
        }
        node->isTerminal = true;
    }
    
    bool search(string word) {
        Node* node = trie;
        for (auto const c:word) {
            int i = c-97;
            if(node->children[i]) {
                node = node->children[i];
            } else {
                return false;
            }
        }
        return node->isTerminal && node->isFound;
    }
    
    bool startsWith(string prefix) {
        
        Node* node = trie;
        for (auto const c:prefix) {
            int i = c-97;
            if(node->children[i]) {
                node = node->children[i];
            } else {
                return false;
            }
        }
        return static_cast<bool>(node);
    }
};
class Solution {
public:
    void search(vector<vector<char>>& board, vector<vector<bool>>& visited, int i, int j, Node* node){
        if (i < 0 || i >= board.size() || j < 0 || j >= board[i].size() || visited[i][j]) return;
        if (node->children[board[i][j]-97]) {
            node = node->children[board[i][j]-97];
            if (node->isTerminal) {
                node->isFound = true;
            }
            visited[i][j] = true;
            search(board, visited, i+1, j, node);
            search(board, visited, i-1, j, node);
            search(board, visited, i, j+1, node);
            search(board, visited, i, j-1, node);
            visited[i][j] = false;
        }
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie *trie = new Trie();
        for(auto const word:words) 
        {
            trie->insert(word);
        }
        
        vector<vector<bool>> visited = vector{board.size(), vector<bool>(board[0].size(), false)};

        for (size_t i = 0; i < board.size(); i++)
        {
            for (size_t j = 0; j < board[i].size(); j++)
            {
                search(board, visited, i, j, trie->trie);
            }
            
        }
        
        vector<string> result{};
        for(auto const word:words) 
        {
            if (trie->search(word)) {
                result.push_back(word);
            }
        }
        return result;
    }
};