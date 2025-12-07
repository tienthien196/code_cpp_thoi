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

 -đối với các method tĩnh thì ko cho phép gọi tahfnh viên normal 
 - đói tưởng sử dụng method tỉnh , không khuyến khích , nên dùng class gọi statiuc thì sẽ tốt hơn  1 phần 
 
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