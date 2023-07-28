//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
#include "gongneng.h"//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
#include <gongneng.h>

using namespace std;

/*
    cout<<"**************"<<endl;
    cout<<"*1. 添加联系人*"<<endl;
    cout<<"*2. 显示联系人*"<<endl;
    cout<<"*3. 删除联系人*"<<endl;
    cout<<"*4. 查找联系人*"<<endl;
    cout<<"*5. 修改联系人*"<<endl;
    cout<<"*6. 清空联系人*"<<endl;
    cout<<"*0. 退出通讯录*"<<endl;
    cout<<"**************"<<endl;
*/
int main()
{
    //通讯录创建
    Contacts ctc;
    //初始化
    ctc.m_Size = 0;

    //定义用户选择
    int select = 0;


    //程序重点：选择编号进行相应功能
    while (true)
    {
        showMenu();
        cin >> select;
        switch (select)
        {
        case 1:     //添加联系人
            addPerson(&ctc);
            break;
        case 2:     //显示联系人
            showPerson(&ctc);
            break;
        case 3:     //删除联系人
            delPerson(&ctc);
            break;
        case 4:     //查找联系人
            findPerson(&ctc);
            break;
        case 5:     //修改联系人
            updatePerson(&ctc);
            break;
        case 6:     //清空联系人
            delContacts(&ctc);
            break;
        case 0:     //退出通讯录
        {
            cout << "感谢使用" << endl;
            system("pause");
            return 0;
        }
            break;
        default:
            break;
        }
    }
    //选择菜单转到相应功能

    system("pause");
    return 0;
}


using namespace std;

/*
    cout<<"**************"<<endl;
    cout<<"*1. 添加联系人*"<<endl;
    cout<<"*2. 显示联系人*"<<endl;
    cout<<"*3. 删除联系人*"<<endl;
    cout<<"*4. 查找联系人*"<<endl;
    cout<<"*5. 修改联系人*"<<endl;
    cout<<"*6. 清空联系人*"<<endl;
    cout<<"*0. 退出通讯录*"<<endl;
    cout<<"**************"<<endl;
*/
int main()
{
    //通讯录创建
    Contacts ctc;
    //初始化
    ctc.m_Size = 0;

    //定义用户选择
    int select = 0;


    //程序重点：选择编号进行相应功能
    while (true)
    {
        showMenu();
        cin >> select;
        switch (select)
        {
        case 1:     //添加联系人
            addPerson(&ctc);
            break;
        case 2:     //显示联系人
            showPerson(&ctc);
            break;
        case 3:     //删除联系人
            delPerson(&ctc);
            break;
        case 4:     //查找联系人
            findPerson(&ctc);
            break;
        case 5:     //修改联系人
            updatePerson(&ctc);
            break;
        case 6:     //清空联系人
            delContacts(&ctc);
            break;
        case 0:     //退出通讯录
        {
            cout << "感谢使用" << endl;
            system("pause");
            return 0;
        }
            break;
        default:
            break;
        }
    }
    //选择菜单转到相应功能

    system("pause");
    return 0;
}
