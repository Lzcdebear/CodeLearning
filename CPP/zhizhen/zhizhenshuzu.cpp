//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int *p = arr;
    cout<<p<<endl;
    cout<<*p<<endl;
    p++;
    cout<<*p<<endl;
    //于是遍历数组变得方便
    int *p2 =arr;
    for (int i =0;i<10;i++)
    {
        cout<<*p2<<endl;
        p2++;
    }
    system("pause");
    return 0;
}
