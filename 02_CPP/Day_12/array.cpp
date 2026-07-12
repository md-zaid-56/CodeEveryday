#include <iostream>
using namespace std;

int main()
{
    int marks[5] = {78, 85, 92, 67, 88};
    cout << "Student Marks:"<<endl;
    for (int i = 0; i < 5; i++)
    {
        cout << "Student " << i + 1 << " : " << marks[i] << endl;
    }
    return 0;
}