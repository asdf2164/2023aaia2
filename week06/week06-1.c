/// week06-1.cpp
#include <stdio.h>
int main(){
    ///陣列宣告+初始值
    ///之前工作缺的作業要記得補交!!!
        int a[4] ={10, 20, 30, 40};
        int b[4]; ///宣告但不指定初始值,即為亂碼
        b[0] = 9;
        b[1] = 8;
        b[2] = 7;
        b[3] = 6;
        for(int i=0;i<4;i++){
            printf("i:%d a[i]:%d b[i]:%d", i, a[i],b[i]);
        }

}
