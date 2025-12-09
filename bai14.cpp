// OOP siêu chi tiéte


/*
- quy tắc của overloading  Function
+ khác nhau về kiểu data, số lượng tam số 
+ khác kiểu trả về  của hàm : không tính 



- overloading Operator
+ định ngĩa trong lớp or hàm ngoài lớp
+ phải trả về kiểu dữ liẹu phù hợp 

? kế thừa toán từ trong cpp diễn ra như thế nào  
- >> << đây là toán tử IO

+ các operator ko thể overload   :: .* ?:
+ các toán tử ko thể overload:
    + - * / % ^
    & | ~ ! , = 
    < > <= >= , ++ , --
    << >> == != && || 
    += -+ /= %= ^=, &= |=
    *= <<== >>== [] ()
    -> ->* , new , new[] delete, delete[]

*/

/*
- học về vecor , list , map
*/

/*Polymorphism
- overloading  và operator loading : thực hiện tại thời diểm biên dịch , compile runtime  
- run time polimorephism  : học về overide function 
+ nếu 1 function virtaul mà ko có body  -> biến class dó thành tính abstract -> lớp interface
+ các function như thế gọi là pure virtaul function
+ ko thể tạo obj từ lớp absstract có pure virtual function 
+ các lớp con phải ghi đề toàn bộ interface

// chưa rõ về pointer và ref trong polimorphism
*/


/*
Abstraction: ẩn đi chi tiêt triển khai , chỉ để lại giao diện
encapsulation : đsong gọi dữ liệu và method  -> cùng kiểm soát và truy cập 

- khi chsung ta trieern khai  interface -> nó chính là  design strategy

-lợi ích của abstract :
    + ko  thể thay đổi dữ liệu nội bộ từ bên ngoài  -> giảm phụ thuọc , ko ảnh hưởng code 
    + dẽ bảo trì , bảo mật

*/

/*
- encapsulation
+ kiểm tra dữ liệu , thay đổi nội bộ không ảnh hưởng đến bên ngoài 
+ giảm sự phụ thuộc,  ngăn chặn truy cập từ bên ngoài


- 2 kxi thuật nâng cao 
+ nested class : class con định nghìa ben trong truy cập toàn bộ được class cha
+ friend function: cho phép 1 hàm bên ngoài  truy cập , chỉ nen dùng khi cac class cần chia sẽ dữ liệu 
*/