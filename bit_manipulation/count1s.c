#include <stdio.h>

int numSetBits(unsigned int A) {
    int count=0;
    while(A!=0)
    {
        if(A&1)
        count++;
        A=(A>>1);
    }
    return count;
}

int main(){
    unsigned int A;
    scanf("%d", &A);
    printf("%d", numSetBits(A));
    return 0;
}
