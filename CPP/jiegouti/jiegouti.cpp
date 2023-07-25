//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

// 结构体的定义
// struct 名字
struct Student
{
    string name;
    int age;
    int score;
}s3;


int main()
{
    // struct 结构体属于用户自定义的数据类型
    // 具体创建
    // struct是可以省略的在创建的时候，但是定义的时候不能省略
    struct Student s1;
    s1.age = 11;
    s1.name = "李四";
    s1.score = 90;
    cout<<s1.name<<" "<<s1.age<<" "<<s1.score<<endl;

    Student s2 = {"张三",10,70};
    cout<<s2.name<<" "<<s2.age<<" "<<s2.score<<endl;
    
    s3.name = "王五";
    s3.age = 24;
    s3.score = 98;
    cout<<s3.name<<" "<<s3.age<<" "<<s3.score<<endl;

    system("pause");
    return 0;
}
