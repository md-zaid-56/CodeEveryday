#include<iostream>
using namespace std;

int calculateBonus(int fixedBonus){
    return fixedBonus;
}

int calculateBonus(int salary, int performance){
    return salary + performance * 500;
}

int calculateBonus(int salary, int performance, int experience){
    return salary + performance * 500 + experience * 500;
}

int main() {
    cout<<"Fixed Bonus(5000) of Employee 1: "<<calculateBonus(2000)<<endl;
    cout<<"Salary is 6000, Performnace is 10 then Bonus of Employee 2: "<<calculateBonus(6000,10)<<endl;
    cout<<"Salary is 10000, Performnace is 8 and Experience is 5 Years then Bonus of Employee 3: "<<calculateBonus(6000,10,5)<<endl;
    
}