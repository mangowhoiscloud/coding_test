#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, sz;
    DSU(int n=0){ init(n); }
    void init(int n){ p.resize(n+1); sz.assign(n+1,1); iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
    void unite(int a,int b){
        a=find(a); b=find(b); if(a==b) return;
        if(sz[a]<sz[b]) swap(a,b);
        p[b]=a; sz[a]+=sz[b];
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; cin >> N >> M;

    int K; cin >> K;          // 진실 아는 사람 수
    vector<int> truth(K);
    for(int i=0;i<K;++i) cin >> truth[i];

    vector<vector<int>> parties(M);
    for(int i=0;i<M;++i){
        int c; cin >> c;
        parties[i].resize(c);
        for(int j=0;j<c;++j) cin >> parties[i][j];
    }

    DSU dsu(N);
    for(auto& v: parties){
        for(int j=1;j<(int)v.size();++j) dsu.unite(v[0], v[j]);
    }

    unordered_set<int> truthRoot;
    for(int t: truth) truthRoot.insert(dsu.find(t));

    int ans = 0;
    for(auto& v: parties){
        bool hasTruth = false;
        for(int x: v){
            if(truthRoot.count(dsu.find(x))){
                hasTruth = true; break;
            }
        }
        if(!hasTruth) ++ans;   // 거짓말 가능 파티
    }
    cout << ans << "\n";
    return 0;
}