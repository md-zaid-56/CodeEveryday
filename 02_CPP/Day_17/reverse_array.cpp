#include<iostream>
using namespace std;

void printArray(int* arr,int size){
    for(int i=0; i<size; i++){
        cout<<arr[i]<<"\t";
    }
    cout<<"\n------------------------------------------------------------------"<<endl;
}

void reverseArray(int* arr,int size){
    int left = 0,right = size-1,temp;
    while(left!=right){
        temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
    printArray(arr,5);
}

int main() {
    int arr[] = {10,20,30,40,50};
    cout<<"--------------------Original Array--------------------\n";
    printArray(arr,5);
    cout<<"\n--------------------Reversed Array--------------------\n";
    reverseArray(arr,5);
    cout<<endl;
    return 0;
}