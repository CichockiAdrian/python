#include<iostream>

using namespace std;

int nwd (int y, int b) // funkcja obliczaj¹ca nwd dwóch liczba - a i b
{
    int c=1;
    if(y==b){
        c=y;
        return c;
    }
    else if(y>b){
        for(int i=1;i<=b;i++){
            if(y%i==0 && b%i==0){
                c=i;
            }
        }
        return c;
    }
    else if(b>y){
        for(int i=1;i<=y;i++){
            if(y%i==0 && b%i==0){
                c=i;
            }
        }
        return c;
    }
}
int nww(int y,int b,int nwd1){
     return y*b/nwd1;
}

int main(){
    int t1[2],t2[2],t3[2];

    cout<<"Podaj licznik i mianownik liczby\n";
    cin>>t1[0]>>t1[1];
    cout<<"Druga liczba\n";
    cin>>t2[0]>>t2[1];
    cout<<"\n Pierwsza liczba ["<<t1[0]<<","<<t1[1]<<"]";
    cout<<"\n druga liczba ["<<t2[0]<<","<<t2[1]<<"]";

    int x= t1[0];
    int y= t1[1];
    int a= t2[0];
    int b= t2[1];



    int nwd1 = nwd(y,b);
    cout<<"\n nwd"<<nwd(y,b);
    int nww1 = nww(y,b,nwd1);
    cout<<"\n nww: "<<nww1;

    t3[0] = (t1[0]*nww1/t1[1])+(t2[0]*nww1/t2[1]);
    t3[1] = nww1;
    cout<<"\n wynik dodawania: ["<<t3[0]<<","<<t3[1]<<"]";

    t3[0] = (t1[0]*nww1/t1[1])-(t2[0]*nww1/t2[1]);
    cout<<"\n wynik odejmowania: ["<<t3[0]<<","<<t3[1]<<"]";

    t3[0] = t1[0]*t2[0];
    t3[1] = t1[1]*t2[1];
    cout<<"\n wynik mnozenia: ["<<t3[0]<<","<<t3[1]<<"]";


    int pom = t2[0];
    t2[0] = t2[1];
    t2[1] = pom;
    t3[0] = t1[0]*t2[0];
    t3[1] = t1[1]*t2[1];
    cout<<"\n wynik dzielenia: ["<<t3[0]<<","<<t3[1]<<"]";

}
