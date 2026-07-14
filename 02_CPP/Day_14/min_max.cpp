#include<iostream>
using namespace std;

int main(){
    int arr[5];
    int min , max;

    for(int i = 0; i < 5; i++){
        cout<<"Enter Element "<<i+1<<" : ";
        cin>>arr[i];
    }

    cout<<endl;
    min=arr[0];
    max=arr[0];
    for(int i = 0; i < 5; i++){
        cout<<"Element "<<i+1<<" : "<<arr[i]<<endl;
        if(min>arr[i]){
            min=arr[i];
        }
        if(max<arr[i]){
            max=arr[i];
        }
    }
    cout<<endl<<"Minimum :"<<min;
    cout<<endl<<"Maximum :"<<max;
    cout<<endl<<"Difference :"<<max-min<<endl;
    return 0;
}