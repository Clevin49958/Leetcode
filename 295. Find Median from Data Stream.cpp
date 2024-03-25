#include <iostream>
#include <vector>
#include <queue>
using namespace std;


class MedianFinder {
public:
    priority_queue<int> lower_queue;
    priority_queue<int, vector<int>, greater<int>> upper_queue;
    int totalSize() {
        return lower_queue.size() + upper_queue.size();
    }

    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (totalSize() % 2 == 0)
        {
            lower_queue.push(num);
        }
        else{
            upper_queue.push(num);
        }
        if (!lower_queue.empty() && !upper_queue.empty() && lower_queue.top() > upper_queue.top())
        {
            int lower_top = lower_queue.top();
            int upper_top = upper_queue.top();
            lower_queue.pop();
            upper_queue.pop();
            lower_queue.push(upper_top);
            upper_queue.push(lower_top);
        }
    }
    
    double findMedian() {
        if (totalSize() % 2 == 0)
        {
            return (lower_queue.top() + upper_queue.top()) / 2.0;
        }
        else{
            return lower_queue.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */