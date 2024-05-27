//fibonaci
#include <iostream>
using namespace std;
int fibonaci(int n){
	int a[n+1];
	a[0] = 0;
	a[1] = 1;
	a[2] = 1;
	for(int i =3; i<n; i++){
		a[i] = a[i-1] + a[i-2];
	}
	return a[n-1];
}
int main(){
	int n;
	cout<<"Nhap n: "; cin>>n;
	cout<<"So fibonaci thu n la: "<<fibonaci(n)<<endl;
	return 0;
}
