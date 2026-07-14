#include<iostream>
using namespace std;

int main(){
    int percentage[5]; //Array of student percentage
    for(int i=0;i<5;i++){  //User Input Array
        cout<<"Enter marks of "<<i+1<<" student : ";
        cin>>percentage[i];
    }
    for(int i=0;i<5;i++){ //Output Printed Using Array
        cout<<endl<<"marks of student "<<i+1<< " : "<<percentage[i];
    }
    cout<<endl;
    return 0;
}