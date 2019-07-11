from cs50 import get_int
import cs50

while True:
    n= get_int("Height:")

    if n>=1 and n<=8:




        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for k in range (n-(n-1)+i):
                print("#", end="")
            print()
        break








