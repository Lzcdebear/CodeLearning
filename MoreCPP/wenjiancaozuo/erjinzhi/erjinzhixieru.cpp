//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

//读取文件前面加上ios::binary
class Person
{
public:
    char m_Name[64];
    int m_Age;
};

void test01()
{
    ofstream ofs;
    ofs.open("F:\\OneDrive\\Coding\\MoreCPP\\wenjiancaozuo\\erjinzhi\\Person.txt",ios::out | ios::binary);
    Person p = {"Zhangsan",18};
    ofs.write( (const char*) &p,sizeof(Person));
    ofs.close();
}


int main()
{
    test01();
    system("pause");
    return 0;
}
