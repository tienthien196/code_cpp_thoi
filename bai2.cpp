// data types Literal TypEs
// bộ nhớ được cáp phát như thế nào 
// giá trị tói thiểu, tối đã mà biến có thể chứa
// phạm vi biến , dùng :: truy cập biến toàn cục
// khởi tạo nhiều biến cùng lúc - khởi tạo nhiều biến cùng giá trị (Multiple variables)
// gán nhiều biến , gán tham số mặc định trong hàm đc 
// dùng biến refence, ref + const biến chỉ đọc, ref arr, ref object

/*
>> Kiểu dữ liệu nguyên thuỷ - Primitive Data Types
bool // true/false
char kí tự đơn 1 byte, pahri dùng trong dấu nháy đơn
int số nguyên 4 bytes
float số thực đơn 4 bytes
double số thực kép 8 bytes
void ko có giá trị- dùng cho hàm không trả về
wchar_t kí tự rộng 2 or 4 bytes dùng cho kí tự Unicode



*/

/* chứa số nguyên , không có phần thập phân
    short int 2 bytes tức là kiểu short - 32,768  32,767
    long int 8 byte(64) or 4 byte (32 bit) tuỳ may
    int 4 bytes -2,147,483,648 2,147,483,647
    unsigned int : chỉ dương không âm 0  4,294,967,295
    unsignned short int 0 - 65,535

*/

/* chứa số thực có phần thập phân
    float 4 bytes + hậu tố f tránh nhầm với double, độ chính xác là 7 chữ số thập phân
    double 8 bytes đọ chính xác cao hơn, độ chính xác là 15 chữ số thập phân
    long double 10 bytes or 16bytes 128 tuỳ máy 

    - chuyển đổi ngầm định  implicit cáting
    - chuyển đọi rõ ràng  explicit casting- ép kiểu 
*/



/* chứa ksi tự duy nhất character
    
    0-9 48- 57
    A-Z 65- 90
    a-z 97- 122
    Escape sequences bắt đầu bàng \ kí tự ko thể nhập trực tiếp
    \\
    \n
    \t
    \"
    \0
    có thể dùng mảng char thay vì dùng thư viện string làm chuỗi
*/

// Derived Data Types
/*
Array - lưu dữ liệu liên tục trong bộ nhớ
Pointer - lưu trữ đia chỉ của 1 biến
Reference - tên khác cho 1 biến đã tồn tại 
*/


// User-Defined Data Type
/*
-Struct : nhóm 1 số kiểu dữ liệu lại với nhau
-class : kết hợp thuộc tính và phương thức
-Union :các biến chia sẽ cùng 1 vùng nhớ
-Enum : là biến số ngyuen bieu dien bang ten , truy cập bằng  ::, chỉ định kiểu cơ số trong enum class
*/


/*
Modifier : dùng trước kiểu cơ bản để thay thế sức chứa

-signed = int : lúc này thì int sẽ chắn chắn là số - orduwong
-unsigned: không dấu chưa 0, nếu truyền âm-> lõi tràn số

-long có thể kết hợp với int
-short nhỏ hơn in

Type qualifiers
-const
-volatitle: biến có thể thay đổi với I/O
-restrit: con trỏ này có thể truy cập vào object

*/

/*
Storage Classes: từ khoá định nghĩa phạm vi scope, phạm vi tồn tại  của biến và hàm
-auto: áp dụng cho biến local, ko thay thời gián tồn tại của biến\
-register: biến được lưu trong register , ko lưu trong Ram, compiler có thểor qua biến nếu khong có register sẵng, không có địa chỉ
- static: duy trì biến tồn tại cho các làn gọi hàm sau
- extern: khai báo biến tàon cục từ file khác, không khởi tạo biến, chỉ tham chiếu
- mutable: định nghĩa biến ,cho phép thay đổi khi là const state của oject, xem fucntion trả về hằng số

*/


/*Constexpr khai báo biến , hàm , contructor là hằng , I/O cố định => thực thi lúc compiler
- biến constexpr chỉ gán hợp lệ với số or biến khái báo constexpr
- hàm constexpr: tham số trả về là literal, không có cin/cout/ sữa biến global [hiệu ứng phụ], chỉ gọi các hàm constexpr
- contructor constexpr: not virtual function, not mutable membeR, not try catch

const có thể tahy đổi lúc runtime-> có thể runtiem oveRhead
constexpr không thẻ thay đổi-> ko có runtime overhead(thời gian phát sinh bộ nhớ)

không hỗ trợ IO
không hỗ trợ bộ nhớ động neW delete
chỉ hỗ trợ liteRal type không hỗ trợ sting , vector
not hỗ trợ try catch

*/



// #include <stdio.h>
#include <iostream>
// #include <cmath>
// #include <ctime>
// #include <cstdlib>

// enum date {
//     thu2, thu3, the4, thu5, thu6
// };
// using namespace std;
// void bto2(int a =9, int n=9);
// int main(){

//     std::cout << ceil(5.2)<< endl;
//     cout  << date::the4;

// }


using namespace std;

int main(){
    int n = 9, &b = n;

    cout << "|" << &n << endl;
    cout << "|" << &b ;
    return 0;
}