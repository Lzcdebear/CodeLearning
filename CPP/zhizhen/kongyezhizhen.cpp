//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    //空指针指向内存地址为0的位置
    //指针无法指向0-255是系统控制的
    int * p = NULL;
    //野指针指向非法的内存空间
    int * q = (int *)0x1100;
    //是一种报错原因，会出现问题，尽量避免
    system("pause");
    return 0;
}
