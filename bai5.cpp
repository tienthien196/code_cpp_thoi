/*Control Statement tóm tắt
 if :kiểm tra 1 đk 
 if.. else  , if else if else
 nested if : lồng if
 switch case default : 1 biến với nhiều giá trị
 nested switch : lofng switch kĩ thậut switch hình cácnh cung 

- lỗi 1 dòng do viết tắt
- lõi dùng == vs =



*/

/*
 - kĩ thuật nested loop gồm 
 nested for loops, nested while loops, nested do while loops
 - lỗi quên break trong switch;

*/

#include <iostream>
#include <string>

using namespace std;

int main(){
    string ti = "tiến ";
    string th = "thiện";

    string new12 = ti + th;
    cout  << new12 << endl;
    cout  << ((string)"tiến "+ (string)"thiện") << endl;

    return 0;
}