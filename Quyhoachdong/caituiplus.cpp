//baitoancaituiphus
#include<bits/stdc++.h>
using namespace std;
class phone{
	public:
		string brand;
		int size;
		int value;
	phone(){
		brand = " samsung";
		size = 0;
		value = 0;
	}	
	phone(string b, int s, int v):brand(b),size(s), value(v){};
	void hienthi(){
		cout<<" #nhan hieu: "<<brand;
		cout<<"; gia ban: "<<value;
		cout<<"; kich thuoc: "<<size<<endl;
	}
};
int n = 6;
phone d[]={
{"samsung",5,10},
{"iphone",6,9},
{"huwei",5,7},
{"xiaomi",9,12},
{"soni",4,5},
{"dell",10,10}
};
int dp[100][100];
int timMax(int n, int max){
	for(int i =1; i<=n; i++){
		for(int j = 1; j<=max; j++){
			dp[i][j] = dp[i-1][j];
			if(d[i-1].size<=j){
				int x =dp[i-1][j-d[i-1].size]+ d[i-1].value;
				int y =dp[i][j];
				dp[i][j] = x>y? x:y;
			}
		}
	}
	return dp[n][max];
}
void hienThiDanhSachDienThoaiDaLay(int n, int max){
	cout<<"Danh sach dien thoai da lay:\n";
	int i = n,j = max;
	while(i>0){
		if(dp[i][j]!=dp[i-1][j]){
			cout<<"dien thoai thu"<<i<<", hang"<<d[i-1].brand<<", gia:"<<d[i-1].value<<endl;
			j-= d[i-1].size;
		}
		i--;
	}
}
int main(){
	for(int i=0; i<n; i++){
		cout<<"dien thoai thu "<<i+1<<endl;
		d[i].hienthi();
	}
	int max = 20;
	cout<<"Tong gia tri max : "<<timMax(n,max)<<endl;
	hienThiDanhSachDienThoaiDaLay(n,max);
	return 0;
}
