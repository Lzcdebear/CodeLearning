//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    //声明一个5元数组
   int arr[5] = {1,3,2,5,4};
    //将数组内元素头尾相反排序
        //记录起始下标
        //记录结束下标
        //起始下标与结束下标互换
        //起始 ++ 结束 --
    int start = 0;
    int end = sizeof(arr) / sizeof(arr[0]) - 1; 
    while (start<end)
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start ++;
        end ++;
   }
   //打印
    for (int i = 0; i<5; i++)
    {
        cout << arr[i];
    }
   system("pause");
   return 0;
}
