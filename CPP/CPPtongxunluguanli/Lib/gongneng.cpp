//这是源文件，输入函数定义，include头文件
#include <gongneng.h>

void showMenu()
{
    cout<<"**************"<<endl;
    cout<<"*1. 添加联系人*"<<endl;
    cout<<"*2. 显示联系人*"<<endl;
    cout<<"*3. 删除联系人*"<<endl;
    cout<<"*4. 查找联系人*"<<endl;
    cout<<"*5. 修改联系人*"<<endl;
    cout<<"*6. 清空联系人*"<<endl;
    cout<<"*0. 退出通讯录*"<<endl;
    cout<<"**************"<<endl;
}


void addPerson(Contacts * ctc)
{
    //判断是否已满
    if (ctc->m_Size == Maxnum)
    {
        cout<<"通讯录已满，无法继续添加"<<endl;
        return;
    }
    else
    {
        cout<<"开始添加";
        //添加
    //姓名--------------------------------------------------
        string name;
        cout<<"请输入姓名："<<endl;
        cin>>name;
        ctc->personArray[ctc->m_Size].m_Name = name;
    //性别--------------------------------------------------
        int sex = 0;
        cout<<"请输入性别："<<endl;
        cout<<"1-----男"<<endl;
        cout<<"2-----女"<<endl;
        while(true)
        {
            cin>>sex;
            if (sex == 1 || sex== 2)
            {
                ctc->personArray[ctc->m_Size].m_Sex = sex;
                break;
            }
            cout<<"输入有误请重新输入"<<endl;
        }
    //年龄--------------------------------------------------
        int age =0;
        cout<<"请输入年龄："<<endl;
        cin>>age;
        ctc->personArray[ctc->m_Size].m_Age = age;
    //电话--------------------------------------------------
        string phone;
        cout<<"请输入电话："<<endl;
        cin>>phone;
        ctc->personArray[ctc->m_Size].m_Phone = phone;
    //地址--------------------------------------------------
        string addr;
        cout<<"请输入地址："<<endl;
        cin>>addr;
        ctc->personArray[ctc->m_Size].m_Addr = addr;
        
        ctc->m_Size ++;
        cout<<"添加成功";
        system("pause");
        system("cls");      //清屏功能
    }
}