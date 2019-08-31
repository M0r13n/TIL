#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

typedef char *string;

/**
 * Checks that the given char is alphabetical.
 * @param c Char to check
 * @return 1 if valid else 0
 */
int is_valid_char(char c)
{
    return (('a' <= c) && (c <= 'z')) || (('A' <= c) && (c <= 'Z'));
}

/**
 * Checks a key and returns 1 if there are only alphabetically chars in it.
 * @param key The key to validate
 * @return 1 if valid else 0
 */
int is_valid_key(string key)
{
    for (int i = 0; key[i] != '\0'; i++)
    {
        if (!is_valid_char(key[i]))
            return 0;
    }
    return 1;
}

/**
 * Print how to use the program and exist with a 1 Exit Code.
 */
void print_usage_and_exit()
{
    printf("Usage: ./vigenere.c key\n");
    exit(1);
}

/**
 * Returns the amount of shifts for a given char.
 * Assumes the char is valid, e.g. ['a-zA-Z']
 * @param c Char to convert
 * @return The amount of shifts
 */
int shift(char c)
{
    if (('a' <= c) && (c <= 'z'))
        return c - 'a';

    return c - 'A';

}

/**
 * Encrypt a text with the Vigenere algorithm.
 * Assumes that the key has been validated before.
 * @param plain_text The text to encrypt.
 * @param key The key used for encryption.
 */
void encrypt(string plain_text, string key)
{
    int cur;
    int k_len = strlen(key);
    int k;
    int pos = 0;
    for (int i = 0; plain_text[i] != '\0'; i++)
    {
        cur = plain_text[i];
        k = shift(key[pos % k_len]);

        if (is_valid_char((char) cur))
            pos++;

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
}


int main(int argc, string argv[])
{
    string plain_text;
    string key;

    // Input validation
    // Input is valid if it is exactly one arg, has at least one letter and contains only letters
    if ((argc != 2) || (!is_valid_key(argv[1])))
        print_usage_and_exit();

    key = argv[1];
    plain_text = get_string("plaintext: ");

    printf("ciphertext: ");
    encrypt(plain_text, key);
    printf("\n");

    exit(0);
}