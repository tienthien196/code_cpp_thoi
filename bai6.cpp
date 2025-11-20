// string trong cpp không bất biến như python \0
// noi chuooi bang toan tu cong  or dung vong lap thu cong 
// so sanh chuoi thi co the dung toan tu so sanh 
/*
- xử lsi chuỗi bằng <cstring> 
- khởi tạo dùng mảng kí tự  c style String
 strcpy(n, n2): sao chép chuối 
 strlen(str): trả về đọi dài chuỗi 
 strcat(n, n2): nối chuỗi 
 strcmp(n, n2): so sánh chuỗi, phan biet hoa thuong 
 strcoll() so sanh thoe quy tat, can conf locate


 - xử lí bằng thư viện <string> an toàn vì tự quản lsi bộ nhớ , chống tràn
 - khởi tạo dùng std::string var= "", std::string var("");
 - xử lí 
    size(), length()
    empty()
    clear();
    find(): tìm vị trí chuỗi con
    substr(pos, n): cắt chuỗi con
    compare(n, n2) return 0 <0 >0
    append(str) noi chuoi, chi dung cho object

 - nhập chuoi
    cin >> s; # dừng khi gặp khoảng trắng 
    getline(cin, s); # dùng cho đọc cả dòng 
 - lặp chuỗi dùng length or range foreach
 - tranh duyet >=size trafn bo nho
 - tranh dung bien dem la int co the bi tran

 - tinh zise string , cpp cos 3 vong lap  


 -cctype thuw vieejn cung cap tolower() toupper()

 - loi 
    so sanh chuoi null,-> luon kiem tra chuooi truoc
    so sanh mang char vs string,  mang char ko co '\0'
    so sanh khong phan biet hoa thuong

*/

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    char str[10] = "hello";
    char str2[10] = "_world";
    
    char str3[30];
    
    strcpy(str3, str);
    cout << str3 << endl;
    cout  << std::string::npos;
}