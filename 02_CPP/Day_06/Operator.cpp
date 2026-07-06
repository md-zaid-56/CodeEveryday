#include<iostream>
using namespace std;

int main()
{
    int a=5,b=2;
    cout<<"Using Addition Operator: "<<a+b<<endl;
    cout<<"Using Subtraction Operator: "<<a-b<<endl;
    cout<<"Using Multiplication Operator: "<<a*b<<endl;
    cout<<"Using Division Operator: "<<a/b<<endl;
    cout<<"Using Modulus Operator: "<<a%b<<endl;

    cout<<"Using Greater Than Operator: "<<(a>b)<<endl;
    cout<<"Using Less Than Operator: "<<(a<b)<<endl;
    cout<<"Using Greater Than or Equal To Operator: "<<(a>=b)<<endl;
    cout<<"Using Less Than or Equal To Operator: "<<(a<=b)<<endl;
    cout<<"Using Equal To Operator: "<<(a==b)<<endl;
    cout<<"Using Not Equal To Operator: "<<(a!=b)<<endl;
    
    cout<<"Using Logical AND Operator: "<<(a>b && a<b)<<endl;
    cout<<"Using Logical OR Operator: "<<(a>b || a<b)<<endl;
    cout<<"Using Logical NOT Operator: "<<!(a>b)<<endl;

}