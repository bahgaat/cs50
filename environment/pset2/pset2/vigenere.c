#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main (int argc, string argv[])
{
  int p;



  {
  if (argc!=2)
  {
      printf("Usage:./vigenere k\n ");
      return 1;
  }


    string k= (argv[1]);
    int lenk= strlen(k);

    for (int i=0; i<lenk;  i++ )
    {

     if(!isalpha(k[i]))
      {
        printf("Invalid key\n");
        return 1;
      }
    }




   string s=get_string();


  for (int i=0, n=strlen(s); i<n; i++)
    {

    if(isalpha(s[i]))
     {
        if(islower(s[i]))
        {

           int x= s[i] -97;
           int f= (x+tolower(k[p])-97)%26;
           int y= f+97;

           printf("%c",y);


        }

        else if(isupper(s[i]))
        {
           int e= s[i] -65;
           int o= (e+toupper(k[p])-65)%26;
           int u= o +65;

           printf("%c",u);


        }
        p = (p+1)%lenk;



    }



}
     printf("\n");
}
}






