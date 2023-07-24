//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
//    这里先解释二维数组的定义方式
//    数据类型 数组名[行数][列数]；
//    数据类型 数组名[行数][列数]={{数据1， 数据2}，{数据3， 数据4}}；
//    数据类型 数组名[行数][列数]={数据1，数据2，数据3，数据4}；
//    数据类型 数组名[][列数]={数据1，数据2，数据3，数据4}；
    int arr[2][3] = 
    {
        {1,2,3},
        {2,5,6}
    };
//    二维数组名称用途
//    查看内存空间大小
//    查看内存首位置
    cout<<sizeof(arr)<<endl;
    cout<<arr<<endl;
    cout<<arr[0]<<endl;
    cout<<arr[1]<<endl;
    system("pause");
    return 0;
}
