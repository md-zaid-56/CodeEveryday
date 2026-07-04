#include<iostream>
using namespace std;

int main()
{
    char name[10];
    int roll;
    cout << "Studing Cout & Cin" << endl;

    cout << "Enter Your Name:";
    cin >> name;

    cout << "Roll no:";
    cin >> roll;

    cout << "Student name is " << name << " and Roll no is " << roll << endl;
    return 0;
}