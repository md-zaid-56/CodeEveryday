#include<iostream>
using namespace std;

int main(){
    int arr[5],sum = 0;
    float average = 0;
    for(int i=0;i<5;i++){
        cout<<"Enter element "<<i+1<<" : ";
        cin>>arr[i];
    }
        for(int i=0;i<5;i++){
        cout<<endl<<" Element "<<i+1<<" : "<<arr[i];
    }
    for(int i=0;i<5;i++){
        sum += arr[i];
    }
    average = (float)sum/5;
    cout<<endl
        <<"Sum = "
        <<sum
        <<endl
        <<"Average = "
        <<average
        <<endl;
    return 0;
}