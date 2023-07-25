//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

struct Student
{
    string name;
    int age;
    int score;
};

int main()
{
    struct Student StuArray[3]=
    {
        {"李四", 11, 90},
        {"张三", 10, 70},
        {"王五", 24, 98}
    };

    StuArray[2].name = "赵六";
    StuArray[2].age = 23;
    StuArray[2].score=10;

    //遍历数组
    for (int i = 0; i<3; i++)
    {
        cout<<StuArray[i].name<<" "<<StuArray[i].age<<" "<<StuArray[i].score<<endl;
    }
    system("pause");
    return 0;
}
