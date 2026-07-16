#include<iostream>
using namespace std;

int main(){
    int arr[] = {5, 10, 15, 20, 25};
    int target,low=0,high=4;
    bool flag = false;
    cout<<"Array is {5, 10, 15, 20, 25}"<<endl;
    
    cout<<"Please Enter Target Element: ";
    cin>>target;

    while(low <= high){
        int mid = (low + high) / 2;

        if(arr[mid]==target){
            flag = true;
            cout<<"\nElement Found";
            cout<<"\nTarget: "<<target;
            cout<<"\nIndex: "<<mid;
            cout<<"\nPosition: "<<mid+1<<"\n";
            break;
        }
        else if(arr[mid]<target){
            low = mid+1;
        }
        else { high = mid - 1;}

    }

    if(!flag){
        cout<<"\nElement Not Found\n";
    }

    return 0;
}