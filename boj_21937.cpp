#include<bits/stdc++.h>

using namespace std;

class Node {
private:
    vector<int> prevTasks;
public:
    void setPrev(int prev) { prevTasks.push_back(prev); }
    void clear(queue<int>& taskQue, vector<bool>& visit) {
        for(auto task: prevTasks){
            if(visit.at(task)) continue;

            taskQue.push(task);
            visit.at(task) = true;
        }
    }
};

int main() {
    int N, M, X, task, nextTask, target, here, ans = 0;
    cin >> N >> M;
    vector<Node> tree(N+1);
    vector<bool> visit(N+1,false);
    queue<int>   taskQue;

    for(int i=0; i<M; i++) {
        cin >> task >> nextTask;
        tree.at(nextTask).setPrev(task);
    }
    cin >> target;
    taskQue.push(target);
    
    while(true) {
        here = taskQue.front();
        taskQue.pop();
        tree.at(here).clear(taskQue, visit);
        if(taskQue.empty()) break;
        ans++;
    }

    cout << ans;

    return 0;
}