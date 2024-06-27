#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){

	
	fstream plik2;
	
	plik2.open("choinka.txt", ios::out);//app
	
	plik2<<" "<<endl;
	plik2<<"         * "<<endl;
	plik2<<"        *** "<<endl;
	plik2<<"      ******* "<<endl;
	plik2<<"    **********"<<endl;
	plik2<<"  ************** "<<endl;
	plik2<<"      *******  "<<endl;
	plik2<<"   ************ "<<endl;
	plik2<<" ***************"<<endl;
	plik2<<"******************* "<<endl;
	plik2<<"        ***         "<<endl;

	plik2.close();


	return 0;
}

