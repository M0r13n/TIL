// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
        node;

// Prototypes
bool load(const char *dictionary);

unsigned int size(void);

bool check(const char *word);

bool unload(void);

unsigned int pos(const char *c);

node *free_node(node *ptr);

unsigned int word_count;

node *create_node(node *ptr);


#endif // DICTIONARY_H
