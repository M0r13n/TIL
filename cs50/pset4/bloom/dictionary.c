// Implements a dictionary's functionality
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdint.h>
#include "dictionary.h"

// Constants
const uint64_t fnv64_prime = UINT64_C(1099511628211);
const uint64_t fnv64_offset = UINT64_C(14695981039346656037);
const int bloom_size = 12345678;

// Structs
typedef struct bloom_filter
{
    void *bits;
    size_t size;
} bloom_filter;

// Variables
unsigned int word_count = 0;
bloom_filter *bloomFilter;

// Prototypes
uint64_t fnv1a64(const char *word);

bool bloom_find(bloom_filter *filter, const char *buffer);

bloom_filter *create_bloom(size_t size);

void bloom_add_hash(bloom_filter *filter, const char *buffer);

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        return false;
    }

    bloomFilter = create_bloom(bloom_size);

    if (!bloomFilter)
    {
        return false;
    }

    char buffer[LENGTH];

    while (fscanf(file, "%s", buffer) != EOF)
    {
        bloom_add_hash(bloomFilter, buffer);

        word_count++;
    }

    fclose(file);

    // Indicate success
    return true;
}

unsigned int size(void)
{
    return word_count;
}

bool check(const char *word)
{
    // Converts string to its lowercase representation
    char copy[strlen(word)+1];
    strcpy(copy, word);
    for (char *p = copy; *p; ++p) *p = tolower(*p);

    return bloom_find(bloomFilter, copy);
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    if (bloomFilter)
    {
        free(bloomFilter->bits);
        free(bloomFilter);
    }

    return true;
}

// ############ Utility Methods ############

// Calculate the FNV hash as suggest by Wikipedia
uint64_t fnv1a64(const char *word)
{
    uint8_t *pointer = (uint8_t *) word;
    uint8_t *buf_end = pointer + strlen(word);
    uint64_t hash = fnv64_offset;

    while (pointer < buf_end)
    {
        hash ^= (uint64_t) * pointer++;
        hash *= fnv64_prime;
    }
    return hash;
}

// Allocates enough memory for a new bloom filter and initialise it with zeros
bloom_filter *create_bloom(size_t size)
{
    bloom_filter *filter = calloc(1, sizeof(bloom_filter));
    filter->size = size;
    filter->bits = calloc(1, size);
    return filter;
}

// Add new word to filter
void bloom_add_hash(bloom_filter *filter, const char *buffer)
{
    unsigned long hash = fnv1a64(buffer);
    uint8_t *bits = filter->bits;
    hash %= filter->size * 8;
    bits[hash / 8] |= (1 << (hash % 8));
}

// Compare a word hash to the filter
bool bloom_find(bloom_filter *filter, const char *buffer)
{
    uint8_t *bits = filter->bits;
    unsigned long hash = fnv1a64(buffer);
    hash %= filter->size * 8;

    // Bitwise AND -> ONLY if result is 1 there is a match
    if (!(bits[hash / 8] & (1 << (hash % 8))))
    {
        return false;
    }

    return true;
}