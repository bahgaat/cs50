from cs50 import get_string
from cs50 import sys
from sys import argv


sys.argv[1]
k=int(sys.argv[1])
if(len(argv))==2:


    s=get_string("plaintext:")
    print("ciphertext:",end="")


    for c in s:




        if c.islower():

            n=ord (c)
            o=n-97
            r=(o+k)%26
            i=r+97
            u=chr(i)
            print(u,end="")


        if c.isupper():

            g=ord (c)
            l=g-65
            j=(l+k)%26
            d=j+65
            w=chr(d)
            print(w,end="")

        if (c==","):

            print(",",end="")

        if (c==" "):

            print(" ",end="")

        if (c=="!"):

            print("!",end="")




    print()
else:
    print("retry")
    exit(2)




