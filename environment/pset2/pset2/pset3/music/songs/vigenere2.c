#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main ( int argc , string argv[])
{
    string s;
    string v;
    int z;
    int l;
    {
    if (argc==2)
    {

    v=argv[1];

     for (int i=0, r=strlen(v);i<r; i++)
     {
         if (islower(v[i]))
         {
             z = v[i]-97;
             s=get_string();
             for (int p=0, n=strlen(s);p<n;p++)
             {
                 if(islower(s[p]))
                 {
                 int x= s[p]-97;
                 int f= (x+z%strlen(v))%26;
                 int y= f+97;

                 printf("%c",y);
                 }
             }
         }
         else if(isupper(v[i]))
         {
             l=v[i]-65;
             s=get_string();
             for (int p=0, n=strlen(s);p<n;p++)
             {
                 if(isupper(s[p]))
                 {
                 int e= s[p]-65;
                 int j= (e+l%strlen(v))%26;
                 int u= j+65;

                 printf("%c",u);
                 }
             }
         }
     }
}
}
}

