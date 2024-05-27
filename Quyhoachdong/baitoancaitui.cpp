#include<bits/stdc++.h>
using namespace std;

int w[] = {5, 10, 6, 3, 7, 8};
int v[] = {15,61, 20, 10, 50, 23};

int a[100][100];

void hienThiMang(int *a, int n) {
  for(int i = 0; i < n; i++) {
    cout << a[i] << "  ";
  }
  cout << endl;
}

// timMax(n, m) la gia tri max nhan duoc cua n goi hang voi gioi han trong luong m 
int timMax(int n, int max) {	
  for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= max; j++) {
	a[i][j] = a[i-1][j];
      if(w[i-1] <= j) {
        int x = v[i-1] + a[i-1][j - w[i-1]];
        int y = a[i-1][j];
        a[i][j] = x > y ? x : y;
      }
    }
  }
  return a[n][max];
}

void hienThiGoiHangDaLay(int n, int max) {
  cout << "Cac goi hang da lay: \n";
  int i = n, j = max;
  while(i > 0) {
    if(a[i][j] != a[i-1][j]) {
      cout << " Goi hang thu " << i
        << ", w = " << w[i-1] 
        << ", v = " << v[i-1] << endl;
      j -= w[i-1];
    }	
    i--;
  }
}

int main() {
  int n = sizeof(w) / sizeof(int),
    max = 15;

  cout << "So goi hang: " << n << endl;
  cout << "Trong luong toi da cua tui: " << max << endl;
  cout << "Thong so cac goi hang lan luot:\n";
  cout << " Weight:\t"; hienThiMang(w, n);
  cout << " Value: \t"; hienThiMang(v, n);

  cout << "\nTong gia tri max lay duoc: " << timMax(n, max) << endl;

  hienThiGoiHangDaLay(n, max);

  return 0;
}
