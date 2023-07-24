#include <iostream>
using namespace std;

int main() {
    int x = 15;

    if (x < 20) {
        cout << "x 小于 20" << endl;

        if (x < 15) {
            cout << "x 小于 15" << endl;
        } else {
            cout << "x 大于等于 15" << endl;
        }
    } else {
        cout << "x 大于等于 20" << endl;
    }

    
   // 局部变量声明
   char grade = 'D';
 
   switch(grade)
   {
   case 'A' :
      cout << "很棒！" << endl; 
      break;
   case 'B' :
   case 'C' :
      cout << "做得好" << endl;
      break;
   case 'D' :
      cout << "您通过了" << endl;
      break;
   case 'F' :
      cout << "最好再试一下" << endl;
      break;
   default :
      cout << "无效的成绩" << endl;
   }
   cout << "您的成绩是 " << grade << endl;

    return 0;
}
