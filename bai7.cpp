// tái sử dụng mã , gọi đc nhìu chõ khác với for lặp
// tách biệt logic, chia nhỏ
// dễ bảo trì  , sữa lỗi 
// tôi ưu hoá


/*
- truyền tham số 
 truyền giá trị call by value -> thay đổi ko ảnh hưởng biến gốc 
 truyền địa chỉ  call by pointer -> ảnh hưởng biến gốc  
 truyền tahm chieu  call by reference, tránh để tham chiếu đến const 

- các tham số mặc định phải được đặt ở cuối danh sách 
- hàm tahm chiếu global
-hàm con trỏ 
- hàm inline
- hàm đẹ quy
    phải có base case để dừng đệ quy 
    mỗi lần gọi đẹ quy phải tiến gần hơn tới base case
- ham lambda

-hàm có số lựng tahm số thay đổi <cstdarg>
    theo ddsung va_start, va_arg, va_end
- hàm mãu template với tahm số biến dỏi variadic template
    dẽ mở rộng , linh hoạt , hỗ trợ nhiều kiểu dữ liệu

- lôi:
    truyen khong khop data type
    tham so mac dinh dat  trước
    định nghia tham số biển đỏi sai 
*/

/* Đệ quy Recursion, gọi alji chính nó với các tham số khác
- base case : đk dừng 
- recursion case , phần cảu hàm nơi nó gọi chính nó với các tham số kahsc nhau
- các lạoi đệ quy 
    direct recursion
    indirect recurrsion 
    nested recursion

- ứng dụng 
    traversal : cây nhị phân
    giải thuật tìm kiếm nhị phân  
    giải thậut : towwer of hanoi

- phải biết khi nào dùng interation , khi nao dùn recursion
- toi ưu bằng 
tail recurrsion
memoizasion
*/

/*
con trỏ -> nó nhảy đwojc đên ô bát kì nhờ đại chỉ  
con trỏ cũng có thể xem ké giá trị , địa chỉ của mấy nhà lân cận  -> gọi là con trỏ mảng 


*/


/*
Function  
- nạp chồng hàm  overload nó không chỉ trong oop mà nó còn trong script thông thường

- hàm truyền tham chiếu  , tham số mặc định , hàm truyền  tham trị
- trong OOP thì có nạp chồng hàm overide từ hàm của class cha  , nếu mà contructor or destructor từ cha  
thì  nó  sẽ chạy contructor của cha trước hay của nó  

- defauilt argument fucntion trong hàm có thể là tham  số mặc định or  là  1 hàm  
nhung mà nếu overload mà tham số  hàm  mặc định giống nahu thì sẽ gay lỗi  đấy   

*/

