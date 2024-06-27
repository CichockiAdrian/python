#include<iostream>
using namespace std;

int main(){
cout<<"iloœæ elementów:";
int n;
cin>>n;
int g, a , x, i, d, m;

cout<<endl;
cout<<"wprowadz elementy";
int T[n];
int D[n];
for(i=0;i<n;i++){
    D[i]=NULL;
}
for(i=0; i<n; i++){

    cin>>T[i];
    }

 for(i=0;i<n;i++){
        for(m=i+1;m<n;m++){
        if(T[m]<T[i]){
            d=T[i];
            T[i]=T[m];
            T[m]=d;
        }
        }
 }
     for(i=0;i<n;i++){
            if(i>=1){
    if(T[i]!=T[i+1]&&T[i]!=T[i-1]){
        D[i]=T[i];
    }
    }
    if(i==0){
    if(T[i]!=T[i+1]){
           D[i]=T[i];
           }
    }
    }

cout<<endl;
cout<<"niepowtarzaj¹ce sie elementy:"<<endl;
for(i=0;i<n;i++){
if(D[i]!=NULL){
cout<<D[i];
cout<<endl;
}
}

}
