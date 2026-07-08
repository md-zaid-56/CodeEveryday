#include<iostream>
using namespace std;

int main(){
    cout<<"Triangle"<<endl;
    for(int i = 1;i<=5;i++){
        for(int j=1;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<endl<<"Reverse Traingle"<<endl;
    for(int i = 5;i>0;i--){
        for(int j = 1 ;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}