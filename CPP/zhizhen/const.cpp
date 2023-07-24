//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    /*
    1. 常量指针
        指针的指向可以改，指针指向的值不能改
        例如
            const int * p = &a
            *p = 20 这是错误的
            p = &b 这是正确的
    2. 指针常量
        指针的指向不能改变，指针指向的值可以改变
        例如
            int * const p = &a
            *p = 20 这是正确的
            p = &b 这是错误的
    3. 
        指针的指向和指针指向的值都不能改
        例如
            const int * const p = &a
    */
    system("pause");
    return 0;
}
