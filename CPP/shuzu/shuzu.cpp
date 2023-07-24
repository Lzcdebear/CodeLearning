#include <iostream>
using namespace std;
 
#include <iomanip>
using std::setw;
 
int main ()
{
   int n[ 10 ]; // n 是一个包含 10 个整数的数组
 
   // 初始化数组元素          
   for ( int i = 0; i < 10; i++ )
   {
      n[ i ] = i + 100; // 设置元素 i 为 i + 100
   }
   cout << "Element" << setw( 13 ) << "Value" << endl;
 
   // 输出数组中每个元素的值                     
   for ( int j = 0; j < 10; j++ )
   {
      cout << setw( 7 )<< j << setw( 13 ) << n[ j ] << endl;
   }
 // 这里的setw就是跟在后面的在距离setw有（）这么多个位置
 // 如果setw后面的长于（）则失去作用
 // 如果小于（）则会自动补充空格
 // 可以使用<<setfill（）后接上 <<setw()来控制setw原本空格位置输出的字符
 
   return 0;
}
