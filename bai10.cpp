/*

Union: bộ nhớ chia sẻ dùng chung
- kich thuoc = thanh vien co kieu lon nhat
- muc dich: dung chung vung nho lon nhat
- ho trợ ghi đè thành viên 
-> tạo  kiểu dữ liệu động 

- union ẩn danh -> để làm kiểu dữ liệu động global 

*/



/*
- con trỏ : nhảy tới nơi khác 
- con trỏ hàm : dùng để return 
- con trỏ biết tiiafn bộ mọi thứ xung quanh ,hàng xóm  ra sao  - con trỏ mảng 
- kxi thuật lsi thuyết :  con trỏ cấp 2 - con trỏ kép


- luôn kiểm tra con trỏ NULL - tránh truy cập con trỏ đá bị giải phóng 
- truy cập thành vien struct = con trỏ 
    dùng (*ptr).member  or dùng ptr->member

- lưu ý về kxi thuạt dùng con trỏ cấp phát động , phải del và đặt null ptr

*/

/*
- các lõi 
truy cập con trỏ nullptr
thao tác với con trỏ đã bị delltete
sữa đổi con trỏ hằng số khong có quyeefn truy cập 
*/


/*
memmory leak : rõ rỉ bộ nhớ
danglijng pointer con trỏ treo: tuỷ cập vào bộ nhớ đã gảiari phóng 
khi chúng ta dùng con tỏ thoong thường -raw pointer : thì phải tự quản lí bộ nhớ -> ssmart pointer
- unique_ptrt : chỉ 1 owener , không thể copy 
- sahre_ptr : chia sẻ ownership bằng refernce counting 
- weak_ptr : tránh dêpndence với sahred_ptr
auto_ptr: đã bị deprecated c++ 11 không nen dùng 

*/

#include <iostream>

using namespace std;

union cache{
    int unit;
    char characters;
};
typedef cache Ca;

typedef struct {
    int bin;
    char cc;
} tienthien;

int main(){

    // cout << " kích thước  của struct" << sizeof(tienthien)<< endl;
    // cout << "kich thước của union" << sizeof(Ca) << endl;

    Ca ca_con;
    ca_con.unit = 15;
    ca_con.characters = 'b';
    cout << ca_con.unit << endl;
    return 0;
}