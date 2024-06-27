#include <iostream>

using namespace std;

int main(){
    int x, y, z;
    x=50;
    y=75;
    cout<<"Poodaj liczbe pomiedzy 50, a 75:";
    cin>>z;

    while(z<50||z>75){
        cout<<"Liczba jest zla, podaj inna:";
        cin>>z;
    }
    if(z>=50&&z<=75){
        cout<<"Liczba "<<z<<" jest poprawna.";
    }
    return 0;
}

