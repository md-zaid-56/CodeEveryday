#include<iostream>
using namespace std;

void printArray(int* arr,int size) {
    cout<<"------------Elements------------\n";
    for(int i=0; i<size; i++){
        cout<<"Element "
            <<i+1
            <<" :"
            <<arr[i]
            <<endl;
    }
    cout<<"--------------------------------\n";
    cout<<"Size of Array inside function :"<<sizeof(arr)<<endl; //it will give output as 8 byte because in c++ we don't pass whole array we just pass the pointer to it
    cout<<"--------------------------------\n";
}

void sumArray(int arr[],int size) {
    int sum = 0;
        for(int i=0; i<size; i++){
            sum =+ arr[i];
    }
    cout<<"Sum of Array: "<<sum<<endl;
    cout<<"--------------------------------\n";
}

int main() {
    int arr[] = { 20, 15, 10, 30, 25};
    printArray(arr,5);
    sumArray(arr,5);
    cout<<"Size of Array outside of a function :"<<sizeof(arr)<<endl; //Here it will be measured in bytes depend to the Datatype we used
    cout<<"--------------------------------\n";    
    return 0;
}