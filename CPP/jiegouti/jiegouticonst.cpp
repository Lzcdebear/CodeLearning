//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

struct student
{
    string name;
    int age;
    int score;
};

void PrintStudent1(student s)
{
    s.age = 100;
    cout<<s.name<<endl<<s.age<<endl<<s.score<<endl;
}

void PrintStudent2(const student * p)
{
    cout<<p->name<<endl<<p->age<<endl<<p->score<<endl;
}


int main()
{
    student s = {"wer",12,45};
    //如果直接使用printstudent则会完全拷贝student，会将数据变得非常大，因为用到的没用到的都会传入
    PrintStudent1(s);
    //而如果使用指针只会传入指针四个字节能节省很多内存空间
    //而且不会复制一个形参出来，节省一个副本
    PrintStudent2(&s);
    //但是如果在函数中改变了数据则会改变s原本的数据
    //为了防止将数据改变则可以在函数定义的时候前面加上 const
    //这样一旦出现改变数据的操作则会报错可以防止误操作
    system("pause");
    return 0;
}
