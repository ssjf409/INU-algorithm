#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
// #include <cstring>

using namespace std;


int N;
vector<long long> costs;
vector<long long> cache;



long long getMinimum(int curIndex) {
    if (costs.size() - 1 == curIndex) {
        return 0;
    }
    
    long long& ret = cache[curIndex];
    if (ret != -1) {
        return ret;
    }

    ret = 1e10;
    long long curCost = costs[curIndex];
    for (int j = curIndex + 1; j < costs.size(); j++) {
        long long nextCost = costs[j];
        long long K = (j - curIndex) * (abs(curCost - nextCost) + 1);
        long long maxVal = max(K, getMinimum(j));
        ret = min(ret, maxVal);
    }
    return ret;
}





int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    cin >> N;
    cache.assign(N, -1);

    long long temp;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        costs.push_back(temp);
    }

    cout << getMinimum(0) << endl;

    return 0;
}