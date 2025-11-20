// +, - ,* , /, %, ++, -- Arithemetic opearator
/*
++, -- nó gán ngay lập tức sau vừa gọi
*/



// toán tử so sánh Relational opearator , logical operator -> trả về true/false, toán tử || khong thể kết hợp với &&
// bitwise & | ^ ~ << >>, giúp thao tác trực tiếp với bit trong bộ nhớ , bitwwise chỉ làm việc với số nguyên 
/*
& and bit 
| or bit
~ đảo tàon bộ bit 0-1 1-0
>> thêm o bên phải
<< thêm o bên trái 
*/

/*
member Operator 
- toán tử dot .
- toán tử arrow -> 

truy cập thành viên *instance.mem  giống với instance->member
biết cách  dùng mảng con trỏ , dung array cap phat ng thay thee 
*/


// gán , gán kết hợp phép toán, gán kết hợp với bitwise

/* Miscelllaeous Operators
- comma operator  dùng để tính toán nhanh trên 1 dòng -> return 1 result
-  :? ternary operator: toán tủ 3 ngôi, toán tử đièu kiện nâng cao dùng nhiều 3 ngôi- conditional operator
- sizeof(var) operator -> trả về bytes của biến , số bytes của biến con trỏ
- :: scope resolution , xác định phạm vi biến hàm , lớp namesapce, tránh xung đột ten, chưa tìm hiểu , cần tìm hiểu bài 43
*/

/*
lỗi thường gặp
- division  by zero 
- overflow tràn số
- a++ + ++a
- số thức ko có toán tử % chia dư
- ptr = 0 con trỏ null tệ -> dùng nullptr
- dịch bit quá nhiều khong chính xác 
- lõi với struct   sử dụgn dot với con trỏ(phải dùng arrow), sử dụng arrow đối với con trỏ(dùng dot opeartor), quên giải phóng bộ nhớ  
- loi truy cap pointer dung voi bien trong scope khac , het scop thi pointer null tranhs, dung pointertruy c cung scope

*/

/* các cách ép kiểu , chuyển đổi kiểu dữ liệu  , và cah chuyển không an toàn 
casting 
const_cast: Thay đổi tính chất const /volatile , sử dụng khi cần thiết▸▸
static_cast: Chuyển đổi kiểu tĩnh, an toàn cho các chuyển đổi hợp lệ▸▸
dynamic_cast: Chuyển đổi kiểu động, chỉ dùng với pointer tham chiếu trong kế thừa▸▸
reinterpret_cast: Chuyển đổi kiểu tái giải thích, sử dụng khi cần thiết và cực kỳ cẩn thận

*/
/* Thu tu uu tien precedence
() [] -> .
++ -- incredent, decrement
! ~  - + dau so nguyen
* / %
+ - toan hang
<< >> 
< <= >= >  == != 
& ^ | && ?:
= += -= *= <<= >>= /=
,
*/



// định nghĩa táon tử trong class 

int createNumber(bool bit1, bool bit2, bool bit3){
    int num =0;
    num |= (bit1 ? 1: 0)<< 0;
    num |= (bit2 ? 1: 0)<< 0;
    num |= (bit3 ? 1: 0)<< 0;

    return num;
}
void bigflag(){
    int flags = 0b00000;
    flags |= 0b0010; //bật bit thứ 2 , flags = flags | 0b0010
    flags &= ~0b0010; //tắt bit thứ 1  
    flags ^= 0b0100; //flags = flags ^ 0b0100
}

#include<iostream>
using namespace std;
struct Employee {
    int kpi =0;
    int salary;
};

// int main(){
//     // cout << (2147483647 + 1 ) << endl;
//     // cout <<(( 0.2 + 0.1) == 0.3)<< endl;
//     cout << ~-6;
//     sizeof(int);
// }

int main(){
    Employee e;
    // e.kpi =90;
    Employee e2;
    // e2.kpi = 100;

    cout << "KPI 1"<< e.kpi << endl;
    cout << "KPI 2" << e2.kpi << endl;


    Employee* p = nullptr;

    p = &e; (*p).kpi = 20;
    p = &e2; (*p).kpi = 30;

    cout << "KPI 1"<< e.kpi << endl;
    cout << "KPI 2" << e2.kpi << endl;



}