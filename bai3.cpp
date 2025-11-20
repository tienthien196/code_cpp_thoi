// các thư viện nhập xuất cpp
// format chuỗi output


/*
#include <iostream> // thư viện cơ bản cho cin/cout
#inlcude <iomanip> // thư viện định dạng xuất(setw, setprecision) format float
#include <fstream> // thư viện cho file I/O

*/

/* iostream
  << toán tử nhập cout, endl dùng để xuóng dòng
  >> toán tử xuất cin, đọc nhiều dòng dùng getline(cin, str)

  cerr << luồng xuất ném lỗi, luồng xuất không đệm , hiển thj err nagy lạp tức
  clog << luồng  ghi nhật kí, dùng cho lỗi + có đệm  

*/

/*Manipulators - bộ điều khiển

*/

/*
Input stream
- ws bỏ qua khoảng trắng trước khi nhập
- noskipws: không bỏ qua khoảng trắng

Output Stream
- setw(n): đặt chiều rộng cho lần hiển thị tiếp theo
- setfill(c) giống ljust của python format string , đi chung vói setw

Alignment
- căn lề dùng chung với setw: left , right,internal điền vào giữa nếu sônguyen có dấu

- endl: chèn dòng mới và flush xoá bộ đếm  
- flush: chỉ xoá bộ đệm
- uppercase
- lowercase
- showpoint số nguyên , thực kế tiếp sẽ hiển thị thập phân
- showpos hiển thị dấu cộng nếu dương

Floating PointeR
-fixed: hiển thị dạng thập phân
- scientific:hiển thị dạng khoa học , exponent
-setprecesion(n): hiển thị số có n chứ số thập phân

Numeric Base
-dec hiê thị dạng thập phân
- oct hiển thị dạng bát phân
- hex hiển thị dạng thập lục
- showbase hiển thị tiền tố hex
Boolean
- boolalpha: hiển thị true false
- noboolalpha: hỉn thị 0 1

Time
- put_time(): định dạng time
- get_time(): phân tíchtime


*/





#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// int main(){
//     float tien = 3.3433;
//     cout  << fixed << setprecision(2) << tien;
//     clog << "tiến thiện ";
// }

// int main(){

//     cout << "thien\n" << flush;
//     cin >> ws;
//     string a;
//     int b= {};
//     getline(cin, a);
    

// }

int main(){
  cout << setfill('*') << setw(10)<< " c c";
  cout << setw(10)<< internal<< -132.9879834<< endl;
}