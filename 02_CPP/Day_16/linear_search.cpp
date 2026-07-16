#include<iostream>
using namespace std;

int main(){
    int arr[5],target,flag=0;
    
    for(int i=0; i<5; i++){
        cout<<"Enter Element "<<i+1<<" : ";
        cin>>arr[i];
    }

    cout<<endl<<"Enter Target element: ";
    cin>>target;
    cout<<endl;

    for(int i=0; i<5; i++){
        if(arr[i]==target){
            flag = 1;
            cout<<"Target: "<<target<<endl;
            cout<<"Position: " <<i+1<<endl;
            cout<<"Index: " <<i<<endl;
            break;
        }
    }
    if(flag==0){
        cout<<"Element Not Found"<<endl;
    }

    return 0;
}