#include<iostream>
using namespace std;

void printEmployeeID(int id){
    cout<<"Employee ID : "<<id<<endl;
    if(id!=1001){ printEmployeeID(id-1); }
}

int sum(int n){
    if(n == 1){ return 1; }
    return n + sum(n-1);
}

int main(){
    cout<<"------------------------------------------------------------------------"<<endl;
    printEmployeeID(1005);
    cout<<"-------------------------------------------------------------------------"<<endl;
    cout<<sum(5)<<endl;
    return 0;
}