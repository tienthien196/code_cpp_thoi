/*Contructor khởi tạo gái trị ban đầu  
- trong cpp ten contructor giống với class  
- không có kiểu trả về  
-  có thể co tham số or không or dèault  cóntructor  
- có thể overload - dùng nhiều tham số khác nhau  

- compieler tự tạo init nếu khong khai báo 

- định nghĩa có 2 cách  : 
set thủ công  
dùng initlication list 
*/

/*Destructor  

- không tham só  , 
không trả về giá trị 
có thể dược overide 
-0> dùng để dọn dẹp và giải phóng tài nguyên  



- khi nàop destructor đc gọi , khi nó ra khỏi scope ko còn biến tahm chiếu  , khi deltete, khi  exit hệ thống 
- thứ tự gọi cóntructor  và destructor  
     cóntructor : cha -> con 
     destructor : con -> cha 
-
 khi sử dụng new phải gọi delete để tránh rò rỉ bọ nhớ 

 Copy constructor  

-implicit : compiler tự tạo shadow copy mặc định 
- explicit : user tự định nghia copy constructor : để quản lí tài nguyên động 

- 2 lỗi với sao chép 
+  doubler -free error : 2 đói tựogn cùng chỉ về 1 vùng nhớ
+ dangling pointer : con trỏ trỏ đến vùng nhớ đã bị giải phóng 






- kĩ thuạt copy đối tượng  -> được gọi  khi passby value ,return obj, được gán obj
- 2 cách sao chép trong cpp 
     + sao chép nông shadow copy sao chép  sao chép dữ liẹu khong sao chép tài nguyên động  
     nếu nhiều biến cùng truy cập vào bộ nhớ chung , tài nguyên có thể bị gải phóng nhiều lần  nếu 1 obj bị huỷ 
     +  deep copy -> sao chép taast cả tài nguyên  , tránh 2 lõi sao chép 
     khi obj bị huỷ mỗi đối ouwjgn sẽ giải phóng 1 vùng nhớ riêng 


 Rule quy tắc 3 
 - kĩ thuạt copy constructor , thì nó nên
 định nghĩa ca  destructor , copy assignment operator( xử lsi gán đối tượng)

Rule quy tắc 5 - nếu lớp hỗ trợ movesenamatic thì cần thêm 
- move cóntructor  chuyển chỗ tài nguyên  
- move assginment  operator  chuyển chỗ tài nguyên khi gán  
 
 
*/



/*
Contructor overloading 
- các cóntructỏ phải đặt gióng tên class  
- mỗi cnsstructor phải khác nhau về số lượgn và kiểu dữ liệu 

Lợi ích khi dùng init  overloading 
đa dạng cách khởi tạo đối tượng -> đa dạng truyền tham số, tuỳ chọn truyền tham số 
tính linh hoạt : đươn giản phần init , 
tính bảo mật : ẩn logic khởi tạu  , tránh sử dụng nhiều setter ()
- hõ trợ tót cho viếcao chép đối tượng 
*/

/*Default argument trong constructor -> tăng tính linh hoạt
- đặc biệt khi có member là const như const property

Delegati Constructor 
- giảm thiếu trùng lặp code constructor  default vs overload
- trong cpp 11 , không dc gọi chính init, gọi 1 constructor khác cùng class
- phải gọi trong initlization list , không thể gọi trogn thân 
- chỉ đc gọi 1 cóntructor khác

- cách dùng : constructor -> gọi constructor chính chưa nhièu feature và default

*/

// tại sao object lại là con trỏ ?khi truyền vào hàm nó mới chỉnh sữa được các thứ khác 