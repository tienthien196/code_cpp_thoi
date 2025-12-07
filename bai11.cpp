/*
- object : cái thực thể mà chúng ta muốn mô phỏng 
- class : bản thiết kế 
- instance : thực thể object được ta ra trong chương trình dựa trên bản thiết kế 

*/


/*
thành viên bao gồm  : data member , member function


public : bên ngoài cóp thể thể dùng thành viên 
private : mặc định , chỉ duy nhát class dùng thành viên
protectectd: chỉ duy nhất class và các class con  dùng đc thành viên 


- contructor , destructor 

*/

// con trỏ truy cạp thành viên như nào 
/* cách định ghĩa class 
- định nghĩa bên trong class thf có phạm vi truy cập 
- định nghĩa bên ngoài dùng classname:: thì ko biét phạm vi truy cập như nào 
thì dùng chức năng default : private
triuy cập : 
- thành viên thừogn thì dùng . dot
- còn tahnfh viên là con trỏ thì truy cập như nào tỏng class 
- tìm hiẻu về con trỏ this trong class này như thế nào 
*/

/* BONUS
- khai abso rõ ràng aceess modifier 
- sử dụng pubic cho các phương thứuc giao diện
- sử dụng private : cho thuọc tính và method nọi bộ

*/


/* 
- bién tĩnh  
chỉ đĩnh nghĩa trong lớp , và gọi khởi tạo bên gnaofi bằng class::member
mặc định biến tĩnh khởi tạo bằng 0 nếu không đượckhowri tạo 


phương thức tĩnh 
- gọi abwfng tên lớp ko cần dối tượng 
- chỉ có thể gọi bằng các thành viên tĩnh khác 
- gọi thẳgng trong dịnh nghĩa , không dùng this vì ko cần đối tượng 


*/

/*
 chú thích thêm thành viên tính  
 -tập trung sử dụng : thành viên thường trong phương thức tính

 -đối với các method tĩnh thì ko cho phép gọi thành  viên normal 
 - object đưuojc sử dụng method tỉnh , không khuyến khích , nên dùng class gọi statiuc thì sẽ tốt hơn  1 phần 
 

 - ứng dụng : quản lí đói tượgn  
 tài nguyên dùng chung resource , singleton duy nhất , cáu hình toàn cuc 
 - có thẻ có const static biến hay khong  , có bín to cục static, có cả static pointer nữa để quản lí tàgi nguyên chung
- dùng trong multihtreading 
 */


/*
method function: hàm thuộc về lớp chứ ko thuộc về đối tượng 
- hàm static : gọi bằng classname::fucntion()
- tiét kiệm bộ nhớ : không cần tạo đói tượng  
- độ an toàn : khong truy cập , không liên qaun đén các tahnh viên not static của class 
- static function khong sử dụng this vì ko liên qaun đến object
- static member fucntion có thể kế thừa nhưung khong polimorphism overide hay loading 

*/

/*
con trỏ this in class , dùng để gọi method tránh xung đột param method
nếu thuộc tính là con trỏ thì sao 
trả về chính đối tượgn thì return *this; cho phép gọi nhiều method 
nhugn mà chúng ta thiết kế class khi nào method nào thì nên trả về con trỏ this chứ 
nhưung nếu return * this mà là method const ->thì sẽ là const myclass ko thể sữa object
- trong đa kế thừa thì  this giúp phân biệt nếu các lớp cha có method cùng tên 

*/

/*HÀM BẠN : cho phép truy cập thuọc tính private từ bên ngoài 
khác báo   friend function trong class trước pahri truyền vào kiểu của class cho friend fucntion
dịnh nghĩa bên ngàoi fucntion

đại khái là kahi báo friebnd fucntion bên trong class để mở cổng \

CLASS BẠN  : cho phép tàon bộ tahfnh viên cảu class có quyền truy cập vào private / protected thành viên của class đánh dáu friend 
chỉ cần tahfnh viên truyền hàm là object của class đánh dầu hàm bjan là dược  ,
và hàm truy cập vì là friend fucntiuon nên đều định nghãi bên ngoài  

class_name::method(objct đánh dấu friend class ))

cùng có thể dùng friend fucntion  trong temaplte classes 
*/


/*
- abstraction : dạng method wrapper  
-> giảm dộ phức tạp  , tăng tích bảo mật , dễ bảo trì 

- encapsulation : ràng buộc toàn vẹn cho dữ liệu
-> dữ liẹu dc bảo vệ bằng privte-> dùng method public để curd

-inhearitance: kế thừa tính ăng từ lớp khác 
-> tái sử dụng code , cáu trúc logic , dễ bảo trì  
code reusability, Logical hierarchy , Easy maintenance

-polymorphism : một phương thức nhiều hình thức 
+ compile time polymorphism : đa hình overrloading  
+ run time polymorphicm : viết đè từ cha : overide 
-> giúp code trở nên linh hoạt -> sử dụng virtaul để cho phép oveeride 
-> sử dụng overide để chỉ rõ phương thức đc overide 

*/

/*
- inline funciton : thay thế gọi hàm bằng code logic trực tiếp  
- trong class thì tát cả method mặc định đã là inline dù ko đăgn kí inline 
-> tăng tốc gọi method của object


- note 
tối ưu cho thực thi , chậm khi biên dịch trình biên dịch có thể bỏ qua yêu cầu  inline 
nê dùng cho các hàm nhỏ và đơn giản  
*/