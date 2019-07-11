#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
int x;
float n;
x=0;
double round(double n);
do
{
n=get_float();
}

while (n<0);
{
n *=100;

}
while (n>=25)
{x++;
 n -=25;
}
while (n>=10)
{x++;
n -=10;
}
while (n>=5)
{x++;
n -=5;
}
while (n>=1)
{x++;
n -=1;
}
printf("%i \n",x);
}