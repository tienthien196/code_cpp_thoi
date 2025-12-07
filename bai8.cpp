/*
mảng nhiều chiều  
a[6][4] = { {}, {}};
size =  tích các chiều  
- đối với mảng 3 chiều trở lên nhìn bằn json sẽ dẽ nhìn hơn // dùng cho đồ hoạ thoi

*/

/*
truyền mảng vào hàm  cũng khá ấy ấy  
- cách 1 truyền bằng con trỏ  
- truyền bằng mảng cố định 
 - truyền mảng khong kích thước  

 mảng 2 chiều 
 -  cách 1 truyền mảng kích thước cố đinh  [m][n]
 - cách 2 truyền  mảng kíhc thước  biến  x, y  , [][y]
- cách truyền mảng với 

nang cao 
- truyền mảng với template
- truyền mảng với std::array  
- truyền mảng với  std:vector  

*/

/*
mảng tromg cpp ko thể trả về trực tiếp  -> lỗi biên dịch
-kích thước của arr ko thẻ xác định tại thời điểm bien dịch 

- giải pháp  
+ viết hàm con trỏ -> hàm trả về kiểu con trỏ -> return arr or arr[0]
vì ddos chính là con trỏ đầu tiên của mảng 
giá trị : thì  arr[0] =  *(arr+0)



- dùng biến static : nhưng biến statisc chỉ tạo 1 lần  
- nên nhiều con trỏ gọi hàm đó thì chỉ truy cập 1 arr duy nhất  
không tốt nêu cần mảng độc lập  

- dùng cấp phát mảng đọng c++  khác C 3 return az với az là con trỏ

- mảng nhiều chiều  - trả về bằng cách dùng cáp phát độg và return về con trỏ cấp  2 
*/