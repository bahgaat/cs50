// Helper functions for music

#include <cs50.h>
#include <math.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    string k=get_string("X/Y");
    while (true);
    {
        if k[2]=8;
        {
            printf("1");
            break;
        }

        else if k[2]=4;
        {
            printf("2");
            break;
        }

        else if k[2]=2;
        {
            printf("3");
            break;
        }

        else if k[2]=1;
        {
            printf("4");
            break;
        }


    }

}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
 char N= note[0];
 int octave = note[strlen(note)-1]-'0';
 int semitone;
 if (N=='C')
 semitone = 1;
 if (N=='D')
 semitone = 3;
 if (N=='E')
 semitone = 5;
 if (N=='F')
 semitone = 6;
 if (N=='G')
 semitone = 8;
 if (N=='A')
 semitone = 10;
 if (N='B')
 semitone = 12;
 if (note[1]=='#')
 semitone++;
 if (note[1]=='b')
 semitone--;
 
 float frequency = 440* (powf(semitone-10)/12));
 return round(frequency * powf(2, octave-4)));
}
 
  
         

// Determines whether a string represents a rest
bool is_rest(string s)
{
   string s=get_string("");

   if (s="\n")
   {
       return ("true");
   }
   else
   {
       return ("false");
   }



}
