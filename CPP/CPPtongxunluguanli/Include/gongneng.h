//这是头文件，输入声明即可
#include <iostream>
using namespace std;

#define Maxnum 1000
//结构体设计
struct Person
{
    string m_Name;
    int m_Sex;      //1 男   2 女
    int m_Age;
    string m_Phone;
    string m_Addr;
};

struct Contacts
{
    Person personArray[Maxnum];
    int m_Size;
};


//函数声明
void showMenu();
void showChange();
void addPerson(Contacts* ctc);
void showPerson(Contacts* ctc);
void delPerson(Contacts* ctc);
void findPerson(Contacts* ctc);
void updatePerson(Contacts* ctc);
void delContacts(Contacts* ctc);
int isExit(Contacts* ctc, string name);
