#include <iostream>

using namespace std;

//int nww(int a, int b){
  //  int c,d;
    //c=a;
    //d=b;
    //while(a!=b){
      // if(a>b)
        //   a-=b;
       //else
         //  b-=a;
    //}
    //return c*d/a
//}
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

    cout<<"znak dzia³ania:"<<endl;
    char z;
    cin>>z;

    int c,d;
    c=t1[1];
    d=t2[1];
    while(a!=b){
       if(a>b)
           a-=b;
       else
           b-=a;
    }
    cout<<c*d/a;
//    switch(z){
 //       case '+':
 //           break;
 //       case '+':
 //           break;
 //       case '+':
 //            break;
 //       case '+':
 //           break;
 //   }

}
