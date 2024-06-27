#include <iostream>

using namespace std;

int nwd(int a, int b){
  do
    {
        if(a > b) {
            a = a - b;
        } else {
            b = b - a;
        }
    }
    while(a != b);
    return a;
}
int main()
{
    int t1[2], t2[2], t3[2];

    cout<<"Podaj licznik i mianownik pierwszej liczby"<<endl;
    cin>>t1[0];
    cin>>t1[1];
    cout<<"Podaj licznik i mianownik drugiej liczby"<<endl;
    cin>>t2[0];
    cin>>t2[1];

    cout<<"Liczba pierwsza: ["<<t1[0]<<","<<t1[1]<<"]"<<endl;
    cout<<"Liczba druga: ["<<t2[0]<<","<<t2[1]<<"]"<<endl;

    cout<<"znak dzialania:"<<endl;
    char z;
    cin>>z;

    int c,d;
    c=t1[1];
    d=t2[1];
    cout<<nwd(c,d);
    switch(z){
        case '+':
            if(nwd(c,d)>1){
                if(c>d){
                    t3[1]=d*nwd(c,d);
                    t3[0]=t1[0]+t2[0]*nwd(c,d);
                }
                else{
                    t3[1]=c*nwd(c,d);
                    t3[0]=t1[0]*nwd(c,d)+t2[0];
                }
            }
            else{
                t3[0]=t1[0]*t2[1]+t2[0]*t1[1];
                t3[1]=t1[1]*t2[1];
            }
            cout<<t3[0]<<"/"<<t3[1];
            break;
        case '-':
            if(nwd(c,d)>1){
                if(c>d){
                    t3[1]=d*nwd(c,d);
                    t3[0]=t1[0]-t2[0]*nwd(c,d);
                }
                else{
                    t3[1]=c*nwd(c,d);
                    t3[0]=t1[0]*nwd(c,d)-t2[0];
                }
            }
            else{
                t3[0]=t1[0]*t2[1]-t2[0]*t1[1];
                t3[1]=t1[1]*t2[1];
            }
            cout<<t3[0]<<"/"<<t3[1];
            break;
        case '*':
            t3[1]=t1[0]*t2[0];
            t3[1]=t1[1]*t2[1];
            cout<<t3[0]<<"/"<<t3[1];
             break;
        case '/':
            break;
        default:
            cout<<"BIm bIM bam bam";
    }

}
