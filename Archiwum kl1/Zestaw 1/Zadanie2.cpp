#include <iostream>

using namespace std;

int main(){
    int a;
    cout<<"Podaj liczbe od 1 do 10: ";
    cin>>a;

    for(int i=0; i<=100; i=i+a){
        cout<<i<<endl;
    }
    return 0;
}
