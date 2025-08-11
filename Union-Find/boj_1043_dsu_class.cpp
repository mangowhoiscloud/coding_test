#include <bits/stdc++.h>
using namespace std;

class DSU {
private:
    vector<int> parent, rank;
public:
    DSU(int n){
        parent.resize(n+1);
        rank.assign(n+1, 1);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x){ 
        return parent[x]==x ? x : parent[x]=find(parent[x]); 
    }

    void unite(int a,int b){
        a=find(a); b=find(b);

        if(a==b) return;
        if(rank[a] < rank[b]) swap(a,b);

        parent[b]=a; rank[a] += rank[b];
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; cin >> N >> M;
    int K; cin >> K;        
 
    vector<int> truth(K);
    vector<vector<int>> parties(M);

    for(auto& t: truth) cin >> t;

    for(int i=0;i<M;i++){
        int c; cin >> c; parties[i].resize(c);
        for(int j=0;j<c;j++) cin >> parties[i][j];
    }

    DSU dsu(N);
    for(auto& party: parties){
        int len = party.size();
        for(int j=1;j<len;j++) 
            dsu.unite(party[0], party[j]);
    }

    unordered_set<int> truthRoot;
    for(int t: truth) truthRoot.insert(dsu.find(t));

    int ans = 0;
    for(auto& party: parties){
        bool hasTruth = false;
        for(int person: party){
            if(truthRoot.count(dsu.find(person))){
                hasTruth = true; break;
            }
        }
        ans += !hasTruth;
    }
    cout << ans << "\n";
    return 0;
}