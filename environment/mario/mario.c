#include <cs50.h>
#include <stdio.h>


int main(void)
{
int n;

do

{
 n=get_int("positive number:");
}
while(n<0 || n>23);

 for (int i=0;i<n;i++)
 {
  for (int j=0;j<n-i-1;j++)
{


printf("-");
}
for (int k=0;k<n-(n-1)+i;k++)
{

 printf("#");
}
for (int r=0;r<n-(n-2);r++)
{
 printf(".");
}
for (int f=0;f<n-(n-1)+i;f++)
{
 printf("#");
}
printf("\n");
}



}
