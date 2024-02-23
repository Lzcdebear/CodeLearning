//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

// 交换两个整数的函数
void swapInt(int &a, int &b)
{
    int temp = a;
    a=b;
    b=temp;
}

// 交换两个浮点型的函数
void swapDouble(double &a, double &b)
{
    double temp = a;
    a = b;
    b = temp;
}

//交换两个任意东西的函数模板
template<typename T>    // 声明一个模板，在代码中的T作为一种通用的数据类型
void mySwap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

void test_01()
{
    int a = 10;
    int b = 20;

    // 自动类型推导的函数模板使用方法
    mySwap(a,b);
    cout<<a<<endl<<b<<endl;

    // 显示指定类型的函数模板使用方式
    mySwap<int>(a,b);
    cout<<a<<endl<<b<<endl;
}

template<typename T>
void mySort(T arr[], int len)   // 从大到小排序
{
    for(int i=0;i<len;i++)
    {
        int max = i;
        for(int j=i+1;j<len;j++)
        {
            if(arr[max]<arr[j])
            {
                max = j;
            }
        }
        if(max != i)
        {
            T temp = arr[i];
            arr[i]=arr[max];
            arr[max]=temp;
        }
    }
}

template<typename T>
void printArray(T arr[], int len)
{
    for(int i=0;i<len;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void test_02()
{
    char charArr[]="vcdefkd";
    int char_num = sizeof(charArr) / sizeof(char);
    mySort(charArr,char_num);
    printArray(charArr,char_num);
}


int main()
{
    // cpp种泛型编程 就是将函数中各种内容进行抽象，具体的确定在实际使用中确定
    test_01();
    test_02();
    system("pause");
    return 0;
}



