    //无论心情怎么样，今天也要继续加油学习哦
    #include <iostream>
    #include <cmath>
    
    using namespace std;
    
    // 常量的定义方式
    // #define 宏常量
    // const 修饰的变量
    // define 的方式是在整个函数全面设置的
    // const 是在函数里定义的
    #define Day 7
    int main()
    {
       cout << Day << endl;
       
       const int Month = 12;
       cout<<"其实c真的不是那么好学，很难的样子";
       cout<<"一年总共有"<<Month<<"月份";
       system("pause");
       return 0;
    }
    
    