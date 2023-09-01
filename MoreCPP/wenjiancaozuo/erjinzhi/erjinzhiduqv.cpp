//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

class Person
{
public:
    char m_Name[64];
    int m_Age;
};

void test01()
{
    ifstream ifs;
    ifs.open("F:\\OneDrive\\Coding\\MoreCPP\\wenjiancaozuo\\erjinzhi\\Person.txt",ios::in|ios::binary);
    if(! ifs.is_open())
    {
        cout<<"open fail"<<endl;
        return;
    }

    Person p;
    ifs.read((char *)&p,sizeof(Person));
    cout<<"Name "<<p.m_Name<<endl<<"Age "<<p.m_Age<<endl;
    ifs.close();
}

int main()
{
    test01();
    system("pause");
    return 0;
}
