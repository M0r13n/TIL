#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

void check(long n)
{
    int cur;
    int prev;
    int l_count = 0;
    int sum = 0;
    int d_digit;

    // Iterate over every decimal value Step-By-Step
    while (n)
    {
        prev = cur;
        cur = n % 10;

        if (l_count % 2)
        {
            d_digit = 2 * cur;
            sum += d_digit % 10;
            if (d_digit >= 10)
                sum += d_digit / 10;
        }
        else
        {
            sum += cur;
        }
        n /= 10;
        l_count++;
    }

    // check if the credit card is valid at all
    if (sum % 10 == 0)
    {
        if (cur == 4 && (l_count == 13 || l_count == 16))
        {
            printf("VISA\n");
        }
        else if (cur == 3 && (prev == 4 || prev == 7) && l_count == 15)
        {
            printf("AMEX\n");
        }
        else if (cur == 5 && prev >= 1 && prev <= 5 && l_count == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
        return;
    }
    printf("INVALID\n");
}

int main(void)
{
    long n = get_long("Number: ");
    check(n);
    exit(0);
}
