#include<iostream>
using namespace std;

char calculateGrade(int marks){
    if(marks<40){ return 'F'; }
    else if(marks>=40 && marks<60){ return 'D'; }
        else if(marks>=60 && marks<75){ return 'C'; }
            else if(marks>=75 && marks<90){ return 'B'; }
                else { return 'A'; }
}

int main() {
    cout<<calculateGrade(30)<<endl;
    cout<<calculateGrade(46)<<endl;
    cout<<calculateGrade(72)<<endl;
    cout<<calculateGrade(81)<<endl;
    cout<<calculateGrade(99)<<endl;
}