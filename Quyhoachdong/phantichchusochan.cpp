#include<bits/stdc++.h>
using namespace std;
int n;
int a[100];
int dem =0;
int chusochan(int n){
	int x;
	if(n<0){
		return 0;
	}
	if (n<10){
		if(n%2==0){
			return 1;
			a[dem++] = n;
			return 1;
		}else{
			return 0;
		}
	}
	
	
	if((n%10)% 2== 0){
		a[dem++] = n%10;
		x= 1;
	}else{
		x= 0;
	}
	return x+ chusochan(n/10);
}
void hien_thi_chu_so_chan(int n){
	int cnt = 0;
	int kq[100];
	while(n>0){
		int r = n%10;
		if(r%2==0){
			kq[cnt++] = r;
		}
		n/=10;
	}
	cout<<"\nSo chu so chan trong n la: "<<cnt<<endl;
	if(cnt>0){
		cout<<"Cac chu so do la: ";
		for(int i =0; i<cnt; i++){
			cout<<kq[i]<<" ";
		}
		cout<<endl;
	}
}
int main(){
	do{
	cout<<"Nhap n\n";
	cin>>n;
	}while(n>2147483647|| n<-2147483647);
	
	cout<<"so chu so chan trong so n la \n";
	cout<<chusochan(n);
	cout<<"\ndanh sach cac chu cai do la \n";
	for(int i =0; i<dem; i++){
		cout<<a[i]<<" ";
	}
	hien_thi_chu_so_chan(n);
}
