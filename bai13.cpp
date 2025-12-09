/*Kế thừa trong cpp 

- Các loại kế thừa  

* công khai : bắt public , bắt protected của base class(cha)
* protected: chỉ bắt public , bắt được protected -> nưhung mà đỏi hết sang protected
* riêng tư  : bắt đựohc public , protected -> sau đó  chuyển hết thành private

- kế thừa nhiều lớp : xung đột trừng tên method
-> dùng scope réolusion :: chỉ định lớp cha nào gọi method 


-note 1 số method đặc biệt khi kế thừa 
hàm tạo 
hàm huỷ 
hàm tạo sao chéo 
tàon tử đc overload  
hàm bạn


- kế thừa là cơ sở cho đa hình overide , phải dùng virtual để cho phép overide 

- kế thừa đa lớp  , note >>  sửdujng virtual if nhiề class parent có cùng base -> hạn chế bọ nhớ 
- cn phải biết về kế thừa đa cấp , in class đa cấp ->>
+ chỉ tổ chức nêu cần thiết , tránh phức tạp hoá 
+ lỗi khi gọi method từ các cấp trên , nhưng trùng tên khác cấp thì vẫn giải quyết bằbg scpoe resolution


*/

/*Các kiểu kế thừa
- single inhertian  : kế thừa từ 1 cha duy nhát 
- kế thừa nhiều  multiple inheritance : ké thừa nhiều lớp cha  -> linh hoạt , phức tạp hoá
- kế thừa đa cấp  multilevel inheritance : môt chuói kế thừa liên tục -> tạo ra hệ thống rõ ràng  
-  kế thừa phân cấp  : hỉearchical inheritance : nhiều con kế thừa từ 1 cha  -> cấu trúc cây


*/