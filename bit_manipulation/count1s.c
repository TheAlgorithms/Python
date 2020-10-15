#include <stdio.h>

int numSetBits(unsigned int A) {
    unsigned int count = 0;
    while(A != 0){
        if(A % 10 == 1)
            count++;
        A /= 10;
    }
    return count;
}

int main(){
    unsigned int A;
    scanf("%d", &A);
    printf("%d", numSetBits(A));
    return 0;
}
