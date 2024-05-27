//bai 1
#include<bits/stdc++.h>
using namespace std;
class quat{
	public:
		string tenhangsx;
		string mausac;
		long giaban;
		quat():tenhangsx(" "),mausac(" "),giaban(0){
		};
		quat(string t,string m, long g):tenhangsx(t),mausac(m),giaban(g){
		};
		void hienthi(){
			cout<<tenhangsx<<setw(10)<<mausac<<setw(10)<<giaban<<endl;
		}
};
int n = 6;
long p = 1000000;
quat d[]= {
{"samsung","do",120000},
{"apple","xanh",150000},
{"Dell","den",200000},
{"panasonic","trang",1500000},
{"LG","den",850000},
{"BIGD","nau",500000}
};
// quat duoc chon
quat s[200];
int k=0;
int c=0;
//quat khong duoc chon
quat u[200];
void sapxep(){
	for(int i=0; i<n; i++){
		for(int j = n-1; j>i; j--){
			if(d[j].giaban<d[j-1].giaban){
				swap(d[j],d[j-1]);
			}
		}
	}
}
void thamlam(){
	cout<<"Tong tien "<<p<<endl;
	sapxep();
	for(int i=0; i<n; i++){
		if(p>= d[i].giaban){
			p-= d[i].giaban;
			s[c++] = d[i];
			
		}
		
	}
	
	cout<<"lay duoc "<<c<<" cai quat:\n";
	cout<<"ten hang sx"<<" "<<"mau sac"<<" "<<"gia ban"<<endl;
	for(int i =0; i<c; i++){
		s[i].hienthi();
	}
}
int main(){
	thamlam();
	return 0;
}
