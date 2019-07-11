#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
   string s;
   {
   if (argc==2)
   {
     string num = argv[1];
     int i= atoi (num);
     s=get_string();
     for (int p=0, n=strlen(s); p<n; p++)
     {
        if(islower(s[p]))
        {
           int x= s[p] -97;
           int f=(x+i)%26;
           int y=f+97;
           printf("%c",y);
        }
        else if(isupper(s[p]))
        {
           int g= s[p] -65;
           int u=(g+i)%26;
           int k=u+65;

           printf("%c",k);

        }

     }
     printf("\n");

}

   else
{
     printf("false\n");
}
}
}