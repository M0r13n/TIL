#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int get_key(string argv[])
{
    char *ptr;
    long k;

    // convert user input to number
    k = strtol(argv[1], &ptr, 10);

    // there may was some malformed input
    if (ptr[0] != 0)
    {
        return 0;
    }
    return (int) k % 26;
}

void print_usage_and_exit()
{
    printf("Usage: ./ceasar key\n");
    exit(1);
}


int main(int argc, string argv[])
{
    int k;
    int len;
    char cur;
    string plain_text;

    // Input validation
    if (argc != 2)
        print_usage_and_exit();

    k = get_key(argv);

    if (k == 0)
        print_usage_and_exit();

    // Encryption Algorithm
    plain_text = get_string("Plaintext: ");
    len = strlen(plain_text);
    printf("ciphertext: ");
    for (int i = 0; i < len; i++)
    {
        cur = plain_text[i];

        if (cur >= 'A' && cur <= 'Z')
        {
            ((cur + k) > 'Z') ? printf("%c", (cur + k) - 'Z' + 'A' - 1) : printf("%c", (cur + k));
        }

        else if (cur >= 'a' && cur <= 'z')
        {
            ((cur + k) > 'z') ? printf("%c", (cur + k) - 'z' + 'a' - 1) : printf("%c", (cur + k));
        }
        else
        {
            printf("%c", cur);
        }
    }
    printf("\n");
    exit(0);
}