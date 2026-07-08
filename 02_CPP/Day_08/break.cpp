#include<iostream>
using namespace std;

int main(){
    for(int i=1001;i<=1010;i++){
        if(i==1005){
            continue;
        }else if(i==1008){
            cout<<"Stolen Vehicle Detected !";
            break;
        }else{
            cout<<"Parking Token: "<<i<<endl;
        }
    }
    return 0;
}