//
// Created by Leon Morten Richter on 13.09.19.
// Usage:   gcc -o shellcode shellcode.c
//          gdb shellcode
//          disassemble main
//

#include <stdio.h>
#include <unistd.h>

int main(void)
{
    char *name[2];

    name[0] = "/bin/sh";
    name[1] = NULL;
    execve(name[0], name, NULL);
}