//
// Created by Leon Morten Richter on 13.09.19.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int
main(int argc, char *argv[])
{
    // printf("Testing%n",&test);
    // schreibt den Wert 6 an die Adresse von Test


    char buf[128]; // this a pointer
    int x;
    int *px = &x;

    *px = 100;

    // -100 = 0xffff + 0xff9c
    // we need to achieve something like this
    *px = 0xff9c;
    *(long *) (((long) &x) + 0x02) = 0xffff;
    printf("x = %d\n", x);
    // end


    if (argc != 2)
    {
        printf("Braucht ein Argument!\n");
        exit(1);
    }

    printf(argv[1]); // vulnerable
    putchar('\n');


    printf("x = %d\n", x);
    printf("Eingabe: ");
    fflush(stdout);

    if (fgets(buf, sizeof buf, stdin)) // reads 128 bytes from stdin and stores it in buf <-> no buffer overflow
        printf(buf); // vulnerable

    printf("x = %d\n", x);

    return 0;
}
