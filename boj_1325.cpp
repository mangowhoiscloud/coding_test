#include<bits/stdc++.h>

using namespace std;

int N, M, pub, sub, maximum=0;

vector<bool> visits;
vector<int> trustScore, answers; 
vector<vector<int>> computers; 

int dfs(int here) {
    visits.at(here) = true;
    int res = 1;

    for(auto row: computers) {
        for(auto com: row) {
            res += dfs(com);
        }
    }

    visits.at(here) = false;
    return res;
}

int main() {
    cin >> N >> M;

    visits.assign(N+1, false);
    computers .resize(N+1);
    trustScore.resize(N+1);

    for(int i=0; i<M; i++){
        cin >> sub >> pub;
        computers.at(pub).push_back(sub);
    }

    for(int i=1; i < N+1; i++) {
        trustScore.at(i) = dfs(i);
        if(trustScore.at(i) == maximum) {
            answers.push_back(i);
        }
        if(trustScore.at(i) > maximum) {
            answers.clear();
            answers.push_back(i);
        }
    }

    for(auto ans: answers) {
        cout << ans << " ";
    }

    return 0;
}