#include<iostream>
#include<cmath>
#include<cstdlib>

using namespace std;

int main(){
    int n,i,m,d;
    int c = 1, k = 1, p =0;
    int o;
    cout<<"iloœæ elementów:";
    cin>>n;
    int T[n];
    cout<<"wprowadz elementy";
    for(int i=0;i<n;i++){
        cin>>T[i];
    }
    cout<<endl;

if(n%2==1){
        o=T[n/2];
        cout<<endl<<"mediana to = "<<o;
    }
    else if(n%2==0){
        o=(T[n/2]+T[n/2-1]);
        cout<<endl<<"mediana to = "<<o;
        o=o/2;
    }
}

