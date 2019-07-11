from cs50 import get_float
while True:
    n=get_float("Change owed:")
    round(n)
    n*=100
    if(n>0):
        x=n%25
        minus = n-x
        z= minus/25

        u=x%10
        minus = x-u
        p= minus/10

        e=u%5
        minus = u-e
        o= minus/5

        g=e%1
        minus = e-g
        d= minus/1

        sum= z+p+o+d
        print(sum)

        break





