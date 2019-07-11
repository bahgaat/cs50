from cs50 import get_string
from cs50 import sys
from sys import argv


def main():
    sys.argv[1]
    k=argv[1]
    if(len(argv))==2:
        file = open(k,"r+")
        lines = [line for line in file.readlines()]
        print("What message would you like to censor?")
        s=get_string()
        x=s.split()
        fullStr =' '.join(lines)
        y = fullStr.split()
        for t in x:
            counter=0
            for w in y:

                q=t.lower()

                if(q==w):

                    r = len(q)
                    print("*"*r, "" ,end="")
                    counter=counter+1

            if(counter==0):
                print( t , "" , end="")

        print()













    else:
        exit(1)









if __name__ == "__main__":
    main()
