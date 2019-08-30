#include <cs50.h>
#include <stdio.h>

// Read user input
int get_input()
{
    int n;

    do
    {
        n = get_int("Height: ");
    } while ((n <= 0) || (n > 8));

    return n;
}

// Print the pyramid
void print_pyramid(int n)
{
    for (int i = 0; i < n; i++)
    {
        // Print first half
        for (int j = 0; j < n; j++)
            (j < (n - i - 1)) ? printf(" ") : printf("#");

        // Print two spaces
        printf("  ");

        // Print second half
        for (int j = 0; j < n; j++)
            if (j <= i)
                printf("#");

        // Print new line
        printf("\n");
    }
}

int main(void)
{
    int n = get_input();
    print_pyramid(n);
    exit(0);
}