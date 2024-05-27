#include <bits/stdc++.h>

const int N = 2000006;

using namespace std;

string s, p;
int Z[N];

void buildZ(const string &s, int Z[]) {
  int n = s.size();
  Z[0] = 0; int l = 0, r = 0;
  for (int i = 1; i < n; ++i) {
    if (r < i) {
      l = r = i;
      while (r < n && s[r - l] == s[r]) ++r;
      Z[i] = r - l; --r;
    } else {
      int k = i - l;
      if (Z[k] < r - i + 1) {
        Z[i] = Z[k];
      } else {
        l = i;
        while (s[r - l] == s[r]) ++r;
        Z[i] = r - l; --r;
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(0); cin.tie(0);
  #ifdef _LAD_
    freopen("SUBSTR.in", "r", stdin);
  #endif
  cin >> s >> p;
  s = p + '#' + s;
  buildZ(s, Z);
  for (int i = p.size() + 1; i < int(s.size()); ++i)
  if (Z[i] >= int(p.size()))
    cout << i - int(p.size()) << ' ';
}

