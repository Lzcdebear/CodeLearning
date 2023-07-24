// 这里展示的是冒泡排序，也就是将一些数字进行大小的排序，也就是升序或者降序
//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
   //利用冒泡排序进行升序的排序
   int arr[9] = {4,2,8,0,5,7,1,3,9};   
   //首先数列是无序的，冒泡的排序方式就是将一个元素与后面所有元素对比直到最后完整
   //排序的总轮数等于元素的个数减一
   //每轮排序的次数等于元素个数减去轮数再减一
   for (int i = 0;i<9;i++)
   {
      for (int j = 0; j<9-i-1;j++)
      {
         //如果第一个数字比第二个数字大，交换两个数字
         if (arr[j]>arr[j+1])
         {
            int temp = arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
         }
      }
   }
   for (int i=0;i<9;i++)
   {
      cout<<arr[i]<<endl;
   }
   system("pause");
   return 0;
}
