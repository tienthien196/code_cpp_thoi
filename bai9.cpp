/*
- nhóm các biến vs nahu  -> giúp code gọn gàng 
- khai bao và khởi tạo biến struct cùng lúc 


- khởi tạo struct thông thường(truy cập bằng  .) và contror struct (truy cập thành viên bằng ->)


*/


/*
dfung type def chó struct -> nếu như này nó khong khởi tạo bién cấu trúc đó cùng lúc được  
*/

/*

- phan biệt mảng struct  -  struct co thành viên là ảmng 
*/

#include <string>
struct Node {
    int data;
    Node* next_node ;
};
typedef Node BIN;
typedef struct {
    string ten ;
    string cache ;
};



#include <iostream>
using namespace std;

int main(){
    
    Node *head  = new Node(); // cấp phát đọng  
    Node v1;
    Node *head  = &v1;

    return 0;
}