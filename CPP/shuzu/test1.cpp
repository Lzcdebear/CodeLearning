//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
   //1. 创建5小猪体重
   int arr[5] = {300,350,400,200,250};
   //2. 找到最大值
   int max = 0;
   for (int i = 0; i<5; i++)
   {
    if (arr[i] > max)
    {
        max = arr[1];
    }
   }
   //3. 输出最大值
   cout <<"最重的小猪的体重为" <<max <<endl;
   system("pause");
   return 0;
}
