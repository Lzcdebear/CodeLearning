//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <fstream>
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
    ifstream filestream;
    //指定打开方式
    filestream.open("F:/OneDrive/Coding/MoreCPP/wenjiancaozuo/duqv/duixiang1.txt",ios::in);
    //判断文件是否打开
    if(!filestream.is_open())
    {
        cout<<"文件打开失败"<<endl;
        return;
    }
    //具体打开方式
    //First
    char buf[1024]={0};
    while(filestream >> buf)
    {
        cout<<buf<<endl;
    }
    //Second
    char buf1[1024]={0};
    while(filestream.getline(buf1,sizeof(buf1)))
    {
        cout<<buf1<<endl;
    }
    //Third
    string buf2;
    while(getline(filestream,buf2))
    {
        cout<<buf2<<endl;
    }
    //Forth
    char c;
    while((c=filestream.get()) != EOF)
    {
        cout<<c;
    }


    //关闭文件
    filestream.close();
    cout<<"file has been closed"<<endl;
}


int main()
{
    test01();
    system("pause");
    return 0;
}
