//这是源文件，输入函数定义，include头文件
#include <gongneng.h>

void showMenu()
{
    cout << "**************" << endl;
    cout << "*1. 添加联系人*" << endl;
    cout << "*2. 显示联系人*" << endl;
    cout << "*3. 删除联系人*" << endl;
    cout << "*4. 查找联系人*" << endl;
    cout << "*5. 修改联系人*" << endl;
    cout << "*6. 清空联系人*" << endl;
    cout << "*0. 退出通讯录*" << endl;
    cout << "**************" << endl;
}


void addPerson(Contacts* ctc)
{
    //判断是否已满
    if (ctc->m_Size == Maxnum)
    {
        cout << "通讯录已满，无法继续添加" << endl;
        return;
    }
    else
    {
        cout << "开始添加";
        //添加
    //姓名--------------------------------------------------
        string name;
        cout << "请输入姓名：" << endl;
        cin >> name;
        ctc->personArray[ctc->m_Size].m_Name = name;
        //性别--------------------------------------------------
        int sex = 0;
        cout << "请输入性别：" << endl;
        cout << "1-----男" << endl;
        cout << "2-----女" << endl;
        while (true)
        {
            cin >> sex;
            if (sex == 1 || sex == 2)
            {
                ctc->personArray[ctc->m_Size].m_Sex = sex;
                break;
            }
            cout << "输入有误请重新输入" << endl;
        }
        //年龄--------------------------------------------------
        int age = 0;
        cout << "请输入年龄：" << endl;
        cin >> age;
        ctc->personArray[ctc->m_Size].m_Age = age;
        //电话--------------------------------------------------
        string phone;
        cout << "请输入电话：" << endl;
        cin >> phone;
        ctc->personArray[ctc->m_Size].m_Phone = phone;
        //地址--------------------------------------------------
        string addr;
        cout << "请输入地址：" << endl;
        cin >> addr;
        ctc->personArray[ctc->m_Size].m_Addr = addr;

        ctc->m_Size++;
        cout << "添加成功";
        system("pause");
        system("cls");      //清屏功能
    }
}


void showPerson(Contacts* ctc)
{
    //判断人数是否为0
    if (ctc->m_Size == 0)
    {
        cout << "当前通讯录为空。" << endl;
    }
    else
    {
        for (int i = 0; i < ctc->m_Size; i++)
        {
            cout << "姓名：" << ctc->personArray[i].m_Name << "\t";
            cout << "性别：" << (ctc->personArray[i].m_Sex == 1 ?"男":"女") << "\t";
            cout << "年龄：" << ctc->personArray[i].m_Age << "\t";
            cout << "电话：" << ctc->personArray[i].m_Phone << "\t";
            cout << "住址：" << ctc->personArray[i].m_Addr << endl;
        }
    }
    system("pause");
    system("cls");
}


int isExit(Contacts* ctc, string name)  //判断联系人是否存在
{
    for (int i = 0; i < ctc->m_Size; i++)
    {
        if (ctc->personArray[i].m_Name == name)
        {
            return i;
        }
    }
    return -1;
}


void delPerson(Contacts* ctc)
{
    cout << "请输入想删除人的姓名：";
    string delname;
    cin >> delname;

    int jugnum = isExit(ctc, delname);
    if (jugnum == -1)  //判断联系人是否存在
    {
        cout << "没有该联系人。" << endl;
    }
    else
    {
        for (int i = 0; i < ctc->m_Size; i++)
        {
            if (ctc->personArray[i].m_Name == delname)
            {
                //将李四后面的数据依次前移一位
                for (int i = jugnum; i < ctc->m_Size; i++)
                {
                    ctc->personArray[i] = ctc->personArray[i + 1];
                }
                ctc->m_Size--;
                cout << "删除成功！";
            }
        }
    }
    system("pause");
    system("cls");
}


void findPerson(Contacts* ctc)
{
    int jumpcir = 0;
    string findname;
    while (jumpcir != 1)
    {
        cout << "请输入想要查找的人的姓名：";
        cin >> findname;
        int jugnum = isExit(ctc, findname);
        if (jugnum == -1)  //判断联系人是否存在
        {
            cout << "没有该联系人。" << endl;
        }
        else
        {
            cout << "姓名：" << ctc->personArray[jugnum].m_Name << "\t";
            cout << "性别：" << (ctc->personArray[jugnum].m_Sex == 1 ? "男" : "女") << "\t";
            cout << "年龄：" << ctc->personArray[jugnum].m_Age << "\t";
            cout << "电话：" << ctc->personArray[jugnum].m_Phone << "\t";
            cout << "住址：" << ctc->personArray[jugnum].m_Addr << endl;
        }
        cout << "继续查找请输入：0" << endl;
        cout << "退出查找请输入：1" << endl;
        cin >> jumpcir;
    }
    cout << "即将返回菜单。" << endl;
    system("pause");
    system("cls");
}


void showChange()
{
    cout << "**************" << endl;
    cout << "*1. 修改姓名*" << endl;
    cout << "*2. 修改年龄*" << endl;
    cout << "*3. 修改性别*" << endl;
    cout << "*4. 修改电话*" << endl;
    cout << "*5. 修改住址*" << endl;
    cout << "*0. 退出修改*" << endl;
    cout << "**************" << endl;
}


void updatePerson(Contacts* ctc)
{
    cout << "请输入想要查找的人的姓名：";
    string originname;
    cin >> originname;

    int jugnum = isExit(ctc, originname);
    if (jugnum == -1)  //判断联系人是否存在
    {
        cout << "没有该联系人。" << endl;
    }
    else
    {
        int jumpcir = 0;
        while (jumpcir != 1)
        {
            {
                cout << "\n \n \n";
                cout << "联系人信息如下" << endl;
                cout << "姓名：" << ctc->personArray[jugnum].m_Name << "\t";
                cout << "性别：" << (ctc->personArray[jugnum].m_Sex == 1 ? "男" : "女") << "\t";
                cout << "年龄：" << ctc->personArray[jugnum].m_Age << "\t";
                cout << "电话：" << ctc->personArray[jugnum].m_Phone << "\t";
                cout << "住址：" << ctc->personArray[jugnum].m_Addr << endl;
                cout << "\n \n \n";
                showChange();
                cout << "请输入想要修改的内容：" << endl;
            }
            int select = 0;
            cin >> select;
            switch (select)
            {
            case 1:     //名字
            {   
                string updatename;
                cout << "输入修改后的姓名：" << endl;
                cin >> updatename;
                ctc->personArray[jugnum].m_Name = updatename;
                break;
            }
            case 2:     //年龄
            {
                int updateage = 0;
                cout << "输入修改后的年龄：" << endl;
                cin >> updateage;
                ctc->personArray[jugnum].m_Age = updateage;
                break;
            }
            case 3:     //性别
            {
                int updatesex = 0;
                cout << "输入修改后的性别：" << endl;
                cout << "1-----男" << endl << "2-----女" << endl;
                cin >> updatesex;
                ctc->personArray[jugnum].m_Age = updatesex;
                break;
            }
            case 4:     //电话
            {
                string updatephone;
                cout << "输入修改后的电话号码：" << endl;
                cin >> updatephone;
                ctc->personArray[jugnum].m_Phone = updatephone;
                break;
            }
            case 5:     //地址
            {
                string updateaddr;
                cout << "输入修改后的住址：" << endl;
                cin >> updateaddr;
                ctc->personArray[jugnum].m_Addr = updateaddr;
                break;
            }
            case 0:     //退出修改
            {
                cout << "即将退出修改联系人" << endl;
                system("pause");
                system("cls");
                jumpcir = 1;
                break;
            }
            default:
                break;
            }
        }
        cout << "\n \n \n";
        cout << "修改已完成，以下是修改后联系人情况：" << endl;
        cout << "姓名：" << ctc->personArray[jugnum].m_Name << "\t";
        cout << "性别：" << (ctc->personArray[jugnum].m_Sex == 1 ? "男" : "女") << "\t";
        cout << "年龄：" << ctc->personArray[jugnum].m_Age << "\t";
        cout << "电话：" << ctc->personArray[jugnum].m_Phone << "\t";
        cout << "住址：" << ctc->personArray[jugnum].m_Addr << endl;
        cout << "即将返回菜单。";
    }
    system("pause");
    system("cls");
}


void delContacts(Contacts* ctc)
{
    int finaljug = 0;
    {
        cout << "******************** WARNING ********************" << endl;
        cout << "是否确定清空通讯录？" << endl;
        cout << "此操作不可逆，将删除通讯录中所有联系人！" << endl;
        cout << "如果希望删除联系人，请输入 0 ，返回菜单后输入 3" << endl;
        cout << "如果希望修改联系人，请输入 0 ，返回菜单后输入 5" << endl;
        cout << "如果为误操作请输入-----0" << endl << "如果确定清空通讯录请输入-----1" << endl;
    }
    cin >> finaljug;
    if (finaljug == 0)
    {
        cout << "清空操作已取消。" << endl;
    }
    else if (finaljug == 1)
    {
        Contacts blankctc;
        *ctc = blankctc;
    }
}