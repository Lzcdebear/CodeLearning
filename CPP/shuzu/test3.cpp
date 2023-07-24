//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    //冒泡排序
    int arr[9]={4,2,8,0,5,7,1,3,9};
    // 开始排序
    for (int i = 0; i<9-1; i++)
    {
        for (int j =0;j<9-i-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j]=arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    system("pause");
    return 0;
}

