#include <iostream>

using namespace std;

int main(){
    int a, x;
    a=55;
    cout<<"Zgadnij liczbe z zakresu od 1 do 100"<<endl;
    cin>>x;
    while(x!=a){
        if (x<a){
            cout<<"Twoja liczba jest za mala"<<endl;
            cout<<"Strzelaj dalej:";
            cin>>x;
        }
        if (a<x){
            cout<<"Twoja liczba jest za duza"<<endl;
            cout<<"Strzelaj dalej:";
            cin>>x;
        }
    }
    cout<<"BINGO!!!Zgadles";
    return 0;
}
