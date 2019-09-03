// Implements a dictionary's functionality
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "dictionary.h"
#include <ctype.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/mman.h>


// Represents a trie
node *root;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    // Initialize trie
    root = create_node(root);
    node *cur = root;

    // Load the file into memory
    char *f;
    struct stat s;
    int fd = open(dictionary, O_RDONLY);

    /* Get the size of the file. */
    int status = fstat(fd, &s);

    if (status != 0)
    {
        unload();
        return false;
    }

    int size = s.st_size;

    // Load the file into memory
    f = mmap(0, size, PROT_READ, MAP_PRIVATE, fd, 0);

    // Numeric Character position in array *children*
    unsigned int c_pos;

    for (int i = 0; i < size; i++)
    {
        if (f[i] == '\n')
        {
            cur->is_word = true;
            cur = root;
            word_count++;
        }
        else
        {
            c_pos = pos(&f[i]);

            // Current character node has not yet been visited and therefore needs to be inserted
            if (cur->children[c_pos] == 0)
            {
                cur->children[c_pos] = create_node(cur->children[c_pos]);

                // Memory Allocation went wrong
                if (cur->children[c_pos] == 0)
                {
                    word_count = 0;
                    return false;
                }
            }
            // Move current node to the corresponding node of the current's character
            cur = cur->children[c_pos];
        }
    }
    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // Traversing is expensive, so store size in a variable and increment it on the fly
    return word_count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Numeric Character position in array *children*
    int c_pos = 0;
    // Current position in word
    int i = 0;
    // Traversal node
    node *cur = root;

    // Loop over each word and check if there is a path in the trie
    while (1)
    {
        c_pos = pos(&word[i]);

        // There may be some weird characters. Catch them!
        if (c_pos > N)
            return false;

        if (!cur->children[c_pos])
        {
            return false;
        }
        cur = cur->children[c_pos];

        // *is_word* needs to be set for the last char of word
        if (word[++i] == '\0')
        {
            if (cur->is_word)
            {
                return true;
            }
        }
    }
}


// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    return free_node(root) == NULL;
}

// ############ Utility Methods ############

// Get numeric representation of a character
unsigned int pos(const char *c)
{
    if (*c == '\'')
    {
        return 26;
    }
    return tolower(*c) - 'a';
}

// Try to create a new node. Return NULL if memory allocation had a problem
node *create_node(node *ptr)
{
    ptr = malloc(sizeof(node));

    // Could not allocate memory
    if (ptr == NULL)
    {
        return NULL;
    }

    // Initialize node
    ptr->is_word = false;

    // Memset is faster than looping
    memset(ptr->children, 0, sizeof(ptr->children));

    return ptr;
}

// Recursive function free every node.
node *free_node(node *ptr)
{
    if (ptr)
    {
        // First free every child, before free the node itself
        for (int i = 0; i < N; i++)
        {
            if (ptr->children[i])
            {
                free_node(ptr->children[i]);
            }
        }
        free(ptr);
    }
    return NULL;
}