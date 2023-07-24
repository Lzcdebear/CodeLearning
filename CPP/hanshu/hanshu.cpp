#include <iostream>
using namespace std;
 
// 函数声明
int max(int num1, int num2);
// 在给函数传输变量值的时候像这样直接传输是引用调用，也就是说改变函数中值不会改变函数外的值
// 如果想让函数内改变的值也传输到外部需要使用例如
// void swap(int &x,int &y)
// 这样的函数才可以
// 也就是添加 &
 
int main ()
{
   // 局部变量声明
   int a = 100;
   int b = 200;
   int ret;
 
   // 调用函数来获取最大值
   ret = max(a, b);
 
   cout << "Max value is : " << ret << endl;
   /*
   []      // 沒有定义任何变量。使用未定义变量会引发错误。
   [x, &y] // x以传值方式传入（默认），y以引用方式传入。
   [&]     // 任何被使用到的外部变量都隐式地以引用方式加以引用。
   [=]     // 任何被使用到的外部变量都隐式地以传值方式加以引用。
   [&, x]  // x显式地以传值方式加以引用。其余变量以引用方式加以引用。
   [=, &z] // z显式地以引用方式加以引用。其余变量以传值方式加以引用。

   [capture](parameters){body}
   []{ ++global_x; }

   [capture](parameters)->return-type{body}
   [](int x, int y){ return x < y ; }
   */

   return 0;
}
 
// 函数返回两个数中较大的那个数
int max(int num1, int num2) 
{
   // 局部变量声明
   int result;

   if (num1 > num2)
      result = num1;
   else
      result = num2;

   return result; 
}