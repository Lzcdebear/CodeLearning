//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int a = 10;
    int * p = &a;
    cout<<sizeof(int *)<<endl;
    cout<<sizeof(float *)<<endl;
    cout<<sizeof(char *)<<endl;
    cout<<sizeof(double *)<<endl;
    system("pause");
    return 0;
}
