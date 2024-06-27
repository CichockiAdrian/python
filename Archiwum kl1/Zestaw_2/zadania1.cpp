#include <iostream>

#include <time.h>

#include <cstdlib>

using namespace std;

int main(){

    srand(time(NULL));

    int m,n, i, j, w;

    j=1;

    w=0;

    m=0;

    cout<<"ile ma byæ elementów "<< endl;

    cin>> n;

    int T[n];

    for(i = 0; i < n; i++){

    T[i] = (rand()%999)+2;


    }
cout<<"liczby pierwsze:"<<endl;
   for(int i=0;i<n;i++){

    while(j<T[i]+1){

    if(T[i]%j==0){

    m++;
}

j++;

}

j=1;

    if(m==2){

    cout<<T[i]<<endl;
    w=w+1;

}

m=0;

}

   cout<<"liczb pierwszysch jest"<<w;

}


