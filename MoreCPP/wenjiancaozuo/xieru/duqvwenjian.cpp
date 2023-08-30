//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;
/*
文件打开的方式
ios::in         读文件而打开文件
ios::out        写文件而打开文件
ios::ate        初始位置为文件尾
ios::app        追加方式写文件
ios::trunc      如果文件存在则先删除再打开
ios::binary     二进制方式打开文件

两种公用方式为  ios::binary | ios::in
*/
void test01()
{
    //创建对象
    ofstream ofs;
    //指定打开方式
    ofs.open("F:\\OneDrive\\Coding\\MoreCPP\\wenjiancaozuo\\duixiang1.txt",ios::out);
    //开始写入内容
    ofs<<"张三 李四 王五"<<endl<<"male male female"<<endl<<"58  57  56"<<endl;
    //关闭文件
    ofs.close();
    cout<<"file has been closed"<<endl;
}


int main()
{
    test01();
    system("pause");
    return 0;
}
