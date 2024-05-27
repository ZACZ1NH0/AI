//phan tich so thanh tong
#include<iostream>
using namespace std;
int soCachPhanTich(int n){
	int a[n+1]={0};
	a[0]= 1;
	for(int i = 1; i<=n; i++){
		for(int j =i; j<=n; j++){
			a[j]+= a[j-i];
		}
	}
	return a[n];
}
int a[100][100];

// f(m, n) la so cach phan tich n thanh cac so nguyen duong <= m
int f(int m, int n) {
  if(m == 0) {
    a[m][n] = (n == 0) ? 1 : 0;
  }
  else {
    if(m > n) {
      a[m][n] = f(m-1, n);
    }
    else {
      a[m][n] = f(m-1, n) + f(m, n-m);
    }
  }

  return a[m][n];
}


int main(){
	int n;
	cout<<"Nhap n"; cin>>n;
	cout<<"So cach phan tich n thanh tong la "<<soCachPhanTich(n)<<endl;
	cout << "So cach phan tich n thanh tong: " << f(n, n) << endl;
	return 0;
}
// 6 = 1 + 1+ 1+ 1+ 1+ 1
//6 = 2 + 1 + 1 + 1+ 1
//6 = 3+ 1+ 1+ 
