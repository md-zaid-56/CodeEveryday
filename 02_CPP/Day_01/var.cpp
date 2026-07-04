#include<iostream>
using namespace std;

int main()
{
    int a = 1;
    float b = 20.5;
    double c = 22.65873582;
    char z = 'Z';
    bool s = false;

    cout<<"Size of Integer a is :"<<sizeof(a)<<endl;
    cout<<"Size of Float b is :"<<sizeof(b)<<endl;
    cout<<"Size of Double c is :"<<sizeof(c)<<endl;
    cout<<"Size of Character z is :"<<sizeof(z)<<endl;
    cout<<"Size of Boolean s is :"<<sizeof(s)<<endl;
    return 0;
}