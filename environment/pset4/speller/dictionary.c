// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;



// Represents a hash table
node *hashtable[N];//similar to olivia
int WORDCOUNT =0;

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;//olivia place
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // TODO


           node *new_node=malloc(sizeof(node));
           if(new_node==NULL)
           {

                unload();
                return false;
           }
           strcpy(new_node->word,word);

           int index = hash(new_node->word);

           if (hashtable[index]==NULL)
           {
               new_node->next =NULL;
               hashtable[index]=new_node;
               WORDCOUNT++;
           }
           else
           {
               new_node->next=hashtable[index];
               hashtable[index]=new_node;
               WORDCOUNT++;

           }




    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if(&load)
    {

        int y=0;
        for( int i=0; i<N; i++ )
        {
            node *cursor = hashtable[i];
            while(cursor!=NULL)
            {
                y++;
                cursor=cursor->next;
            }

        }
        return y;


    }

    else
    {
        return 0;
    }


}

// Returns true if word is in dictionary else false
bool check(const char *word)
{

    int index= hash(word);
    node *cursor= hashtable[index];

    while (cursor!=NULL)
    {
        char tempword[LENGTH+1];
        //strcpy(tempword, word);
        for(int i=0, n=strlen(word);i<=n; i++)
        {
            tempword[i]=tolower(word[i]);
        }
        if(strcmp(tempword,cursor->word) == 0)
        {
            return true;
        }
        else
        {

            cursor=cursor->next;
        }

    }

    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i= 0; i< N; i++)
    {
        node *cursor = hashtable[i];
        while(cursor!=NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }

    }
    return true;
}
