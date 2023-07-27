//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

/*
{"liubei",23,"man"}
{"guanyv",22,"man"}
{"zhangfei",21,"man"}
{"zhaoyun",21,"man"}
{"diaochan",19,"woman"}
*/

//英雄结构体
struct Hero
{
    string name;
    int age;
    string sex;
};

void bubbleSort(struct Hero heroarray[], int len)
{
    for (int i = 0; i<len; i++)
    {
        for (int j = 0; j<len-i-1;j++)
        {
            if (heroarray[j].age > heroarray[j+1].age)
            {
                struct Hero temphero;
                temphero = heroarray[j];
                heroarray[j] = heroarray[j+1];
                heroarray[j+1] = temphero;
            }
        }
    }
}

void printHero(struct Hero heroarray[], int len)
{
    for (int i=0;i<len;i++)
    {
        cout<<"name "<<heroarray[i].name<<" age "<<heroarray[i].age
            <<" sex "<<heroarray[i].sex<<endl;
    }
}

int main()
{
    //结构体
    //数组
    Hero heroarray[5] = 
    {
        {"liubei",23,"man"},
        {"guanyv",22,"man"},
        {"zhangfei",21,"man"},
        {"zhaoyun",21,"man"},
        {"diaochan",19,"woman"}
    };

    int len = sizeof(heroarray) / sizeof(heroarray[0]);
    //年龄排序
    bubbleSort(heroarray,len);
    printHero(heroarray,len);
    system("pause");
    return 0;
}
