#include <iostream>

// chú ý 
/*
>> đặt tên biến  
- RULE
    bắt đầu đúng cách :
        phải bắt đầu A-Z a-z or underscope
        không được bắt đàu bằng số
    phần còn lại 
        có thể chứa chứ các, chữ só , _
        không chứa khoảng trắng hay kí tự đặc biệt @, #, $ , -...
    độ dài :
        không có giới hạn cụ thể
        tốt nhất không quá 30 kí tự
- dùng camelcase, snake_case, hằng số viết hoa
- trong chương trình tên tự đặt , thì gọi là  identifiers
>> 
Miscellaneous Keywords
-namespace: tránh xung đột tên
-using: dùngkhong cần khai báo đầy đủ
-typedef: tên thay thế chi kiểu dữ liệu 
-declttype: xác định kiểu của 1 biểu thức
-static_assert: kiểm tra điều kiện tại thời điểm biên dịch
-constans: hằng số ,literals: giá trị hằng số

const: có biến và kiểu dữ liệu rõ ràng  
#define- thay thế văn bản
*/ 

/*
>>kiểu dữ liệu 
int, long, 
sort,
char kí tư 1, 
double thực 8, 
float thực 4 hậu tố f, 
bool, 
void-> dùng cho hàm ko có giá trị, 
- biểu diễn số nguyên : nhị phân , bát phân , thập phân
- phân biệt int- long -> dùng hậu tố  

u là unsign l là long - có thể dùng U L or kết hợp cả 2 
- biểu diễn số thực , exponent, hậu tố f L, long double

- biểu diễn kí tự char  newline'\n' tab'\t' quote'\'' 
\n newline
\t tab
\\ backslash
\" nháy kép
\' nháy đơn
\a alert
\0 null character
*/ 

/*
>>toán tử , toán hạng

- số học - arithmetic operators
- so sánh- relational operators
- logical
- bitwwise
- dấu câu  ; , . () {} []
*/ 

/*
>> thao tác
-if else switch case default 
-for while do-while
break: thoát khỏi lặp, 
continue: bỏ qua lặp, 
return: trả về giá trị, 
goto: nhảy đến nhãn

-try: bắt ngoại lệ  
-catch: xử lí ngoại lệ
-throw: ném ngoại lệ

- semilicon: dấu kết thúc ;
- blocks: scope phạm vi lệnh
*/

/*
>>gói lại trong OOP
class định ngĩa lớp private mặc định ,
struct: định nghĩa cấu trúc public mặc dịnh , 
union : chia sẻ bộ nhớ giữa các thành viên
enum : định nghia kieu kieu liet ke

this -> trỏ đến đối tượng hện tại
protected, public , private, virtual, friend
- lớp: bản mãu để tại ra các đối tượng, định nghĩa METHOD VÀ PROPERTIES cho đối tượng
- đối tượng: là một thực thể có trạng thái và hành vi
- method : là một hàm trong lớp 

- 

- kế thừa
- đóng gói 
- đa hình 


*/

/*
>>quản lí bộ nhớ
new cấp phát bộ nhớ động . 
delete: giải phóng bộ nhớ

- con trỏ , tham chiếu 

- static: biến giá trị biến vẫn đưuojc lưu sau gọi hảm  
- auto : biến tự định nghĩa kiểu dữ liệu, phải chứa state trước
- register: biến gợi ý biến trong CPU register
- extern: biến đc định nghĩa ở file khác
- mutable



*/



/*
>> Cáu trúc dữ liệu và thuật táon 
vector , list, map, sort, find
<vector>, <algorithms>, từ kháo  uato
*/

/*
>> template

*/


int main(){

    return 0;
}