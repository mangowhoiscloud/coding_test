#include <bits/stdc++.h>
using namespace std;

// Topological order + DP over ancestors sets.
// For each edge v->u: anc[u] |= anc[v]; anc[u].set(v);
// n <= 1000 (fits bitset<1000>).
class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> dag(n);
        vector<int> indeg(n, 0);
        for (auto &edge : edges) {
            dag[edge[0]].push_back(edge[1]);
            ++indeg[edge[1]];
        }

        vector<bitset<1000> > ancestors(n);
        queue<int> q;
        for (int i = 0; i < n; ++i) if (indeg[i] == 0) q.push(i);

        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (int u : dag[v]) {
                ancestors[u] |= ancestors[v];  // all v's ancestors are also u's
                ancestors[u].set(v);     // v itself is an ancestor of u
                indeg[u]--;
                if (indeg[u] == 0) q.push(u);
            }
        }

        vector<vector<int>> ans(n);
        for (int v = 0; v < n; ++v) {
            for (int x = 0; x < n; ++x)
                if (ancestors[v].test(x)) ans[v].push_back(x); 
        }
        return ans;
    }
};

#ifdef LOCAL_TEST
// Local quick test. Compile with: -DLOCAL_TEST
int main() {
    int n = 8;
    vector<vector<int>> edges = {
        {0,3},{0,4},{1,3},{2,4},{2,7},{3,5},{3,6},{4,6}
    };
    Solution s;
    auto out = s.getAncestors(n, edges);
    for (int i = 0; i < n; ++i) {
        cout << i << ":";
        for (int a : out[i]) cout << " " << a;
        cout << "\n";
    }
    return 0;
}
#endif
