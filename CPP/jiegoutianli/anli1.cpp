//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
#include <ctime>

using namespace std;

struct student
{
    string sName;   //学生姓名
    int score;      //学生成绩
};
//老师的结构体
struct teacher
{
    string name;        //老师姓名
    student sArray[5];  //老师带的学生
};

//赋值
void allocateSpace(teacher tarray[], int len)
{
    string nameseed = "ABCDEFGH";
    for(int i = 0 ; i < len; i++)
    {
        tarray[i].name = "Teacher_";
        tarray[i].name += nameseed[i];

        for (int j=0;j<5;j++)
        {
            tarray[i].sArray[j].sName = "Student_";
            tarray[i].sArray[j].sName += nameseed[j];

            int random = rand()%61+40; // 40-99
            tarray[i].sArray[j].score = random;
        }
    }
}

void printinfo(teacher tarray[], int len)
{
    for (int i = 0;i<len;i++)
    {
        cout<<tarray[i].name<<endl;
        for (int j =0;j<5;j++)
        {
            cout<<tarray[i].sArray[j].sName<<"  "<<tarray[i].sArray[j].score<<endl;
        }
    }
}


int main()
{
    //随机数种子
    srand((unsigned int)time(NULL));
    //3个老师的数组
    teacher tArray[3];
    //3个老师信息，学生信息
    int len = sizeof(tArray) / sizeof(tArray[0]);
    allocateSpace(tArray,len);
    //打印老师学生信息
    printinfo(tArray,len);
    system("pause");
    return 0;
}
