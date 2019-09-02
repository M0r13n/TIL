// Implements a dictionary's functionality
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "dictionary.h"
#include <ctype.h>

// Represents a trie
node *root;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = create_node(root);

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];
    // Traversal Node
    node *cur = root;
    // Numeric Character position in array *children*
    unsigned int c_pos;
    // Current Position in word
    int i = 0;

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        cur = root;
        i = 0;
        while (1)
        {
            c_pos = pos(word[i]);

            // Current character node has not yet been visited and therefore needs to be inserted
            if (cur->children[c_pos] == NULL)
            {
                cur->children[c_pos] = create_node(cur->children[c_pos]);

                // Memory Allocation went wrong
                if (cur->children[c_pos] == NULL)
                {
                    word_count = 0;
                    return false;
                }
            }
            // Move current node to the corresponding node of the current's character
            cur = cur->children[c_pos];

            // Current character is last character
            if (word[++i] == '\0')
            {
                cur->is_word = true;
                break;
            }
        }
        // If everything went okay, increase the wordcount;
        word_count++;
    }
    // Close dictionary
    fclose(file);

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
        c_pos = pos(word[i]);

        // There may be some weird characters. Catch them!
        if ((c_pos < 0) || (c_pos > N))
            return false;

        if (cur->children[c_pos] == NULL)
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
unsigned int pos(char c)
{
    if (c == '\'')
    {
        return N - 1;
    }
    return tolower(c) - 'a';
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
    for (int i = 0; i < N; i++)
    {
        ptr->children[i] = NULL;
    }
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
            if (ptr->children[i] != NULL)
            {
                free_node(ptr->children[i]);
            }
        }
        free(ptr);
    }
    return NULL;
}