#include<iostream>
using namespace std;

int main(){
    int a = 18 ;
    float b = a; //implicit conversion;
    cout<<"A="<<a<<" B="<<b<<endl;

    float c =  3.14567;
    int d  =  (int)c; //Explicit Casting
    cout<<"C="<<c<<" D="<<d<<endl;
    
    int z = 5;
    double s = 7.87256;
    cout<<(s+z)<<endl; //Type Promotion
}