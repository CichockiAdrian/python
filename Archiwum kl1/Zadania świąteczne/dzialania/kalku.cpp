#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){
	  string z;
    int l, i, w;
    fstream plik;
    fstream plik2;
    plik.open("dzialania.txt", ios::in);
    plik2.open("wyniki.txt", ios::out);

 

    for(int q=0;q<5;q++){
      plik>>l;
		  plik>>z;
    	plik>>i;
    	
    	
	
    if(z=="dodac"){
        w=l+i;
        plik2<<w<<endl;
    }
   else if(z=="odjac"){
        w=l-i;
        plik2<<w<<endl;
    }
    else if(z=="mnoz"){
        w=l*i;
        plik2<<w<<endl;
    }
    else if(z=="dziel"){
        w=l/i;
        plik2<<w<<endl;
    }
    else{
    plik2<<"blad"<<endl;
    }

 

    }
    plik.close();
    plik2.close();
return 0;
}
