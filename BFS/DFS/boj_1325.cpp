#include<bits/stdc++.h>
#define MAX_N 10004

using namespace std;

int N, M, pub, sub, maximum=0;

bool visits[MAX_N] = {false, };
int  trustScore[MAX_N] = {0,};
vector<vector<int>> computers; 

int dfs(int here) {
    visits[here] = true;
    int res = 1;

    for(auto sub: computers.at(here)) {
        if(visits[sub]) continue;
        res += dfs(sub);
    }

    return res;
}

int main() {
    cin >> N >> M;
    computers .resize(N+1);

    for(int i=0; i<M; i++){
        cin >> sub >> pub;
        computers.at(pub).push_back(sub);
    }

    for(int i=1; i < N+1; i++) {
        fill(visits, visits+N+1, 0);
        trustScore[i] = dfs(i);
        maximum = max(trustScore[i], maximum);
    }

    for(int i=1; i < N+1; i++) {
        if(trustScore[i] == maximum) cout << i << " ";
    }

    return 0;
}