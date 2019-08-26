# Strings in C
There is no native primitive data type for strings in C. 
Instead strings are stored as an array of individual chars with 1 byte each.
**BUT** there is a trick to introduce a string like datatype, so that things become a lot clearer when writing code.
Arrays can be instantiated with values assigned, like `int x[3] = {1, 2, 3};`. 
So it is possible to do:

```c
#include <stdio.h>

typedef char *string;

int main()
{
    char test[] = "Some text\n";
    string text = test;

    printf("%s", text);
    printf("%s", test);
    printf("%i", test == text); // True
    return 0;
}
```