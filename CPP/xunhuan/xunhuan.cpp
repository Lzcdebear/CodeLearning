//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
#include <cctype>
using namespace std;

int main()
{
    int a = 10;
    while (a<20)
    {
        cout<<a<<endl;
        a++;
    }

    for (int a = 10; a<20; a++)
    {
        cout <<a <<endl;
    }

    int my_array[5]={1,2,3,4,5};
    for (int &x : my_array)
    {
        x *= 2;
        cout<<x<<endl;
    }

    string str("some strings");
    for (auto &c:str)
    {
        c = toupper(c);
    }
    cout <<str<<endl;

    return 0;
}

