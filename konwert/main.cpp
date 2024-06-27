#include <iostream>

using namespace std;

int main()
{
    long long n;
    cout << "Enter a binary number: ";
    cin >> n;

    int dec = 0, i = 0, rem;

    while (n!=0) {
    rem = n % 10;
    n /= 10;
    dec += rem * pow(2, i);
    ++i;
  }


    cout << n << " in binary = " << dec << " in decimal";
    return 0;
}
