#include <string>

using namespace std;

class Trie {
public:

    struct Node {
        Node* children[26];
        bool isTerminal = false;
    };
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
        return node->isTerminal;
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

int main()
{
    Trie trie = *new Trie();
    trie.startsWith("a");
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app"); 
}
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */