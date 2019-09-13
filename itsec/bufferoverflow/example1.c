//
// Created by Leon Morten Richter on 13.09.19.
//
#include <stdio.h>
void function(int a, int b, int c)
{
    // stack: [buffer2] [buffer1] [sfp] [ret] [args...]
    char buffer1[5]; // takes a total of 8 bytes & sfp takes 4 bytes -> 12 bytes
    char buffer2[10];
    char *ret;

    ret = buffer1 + 12;
    (*ret) += 8;
}

int main(void)
{
    int x;

    x = 0;
    function(1, 2, 3);
    x = 1;
    printf("%d\n", x);
}