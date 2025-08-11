#include<vector>
#include<bitset>
#include<queue>

using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        bitset<10000> visited, masterK; queue<int> q;
        int here = 0, n = rooms.size();

        
        q.push(here); masterK.set(here);

        while(!q.empty()) {
            here = q.front(); q.pop();
            visited.set(here);
            for(int i=0; i<rooms[here].size(); i++) {
                int key = rooms[here][i];
                if(visited.test(key)) continue;
                if(masterK.test(key)) continue;
                q.push(key); masterK.set(key);
            }
        }

        for(int i=0; i<n; i++) {
            if(!visited.test(i)) return false;
        }

        return true;
    }
};