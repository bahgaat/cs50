def lines(a, b):
    """Return lines in both a and b"""
    x= a.splitlines( )
    y= b.splitlines( )
    res= set(x).intersection(y)
    return res




def sentences(a, b):
    from nltk.tokenize import sent_tokenize
    x=sent_tokenize(a)
    y=sent_tokenize(b)
    res2= set(x).intersection(y)
    return res2

def substrings(a, b, n):
    list1=[ ]
    for i in range(len(a)):
        if len(a)==n:
            list1.append(a[i:n+i])
            break
        elif len(a) < n:
            break
        elif len(a[i:n+i])<n:
            break
        else:
            list1.append(a[i:n+i])

    list2=[ ]
    for i in range(len(b)):
        if len(b)==n:
            list2.append(b[i:n+i])
            break
        elif len(b) < n:
            break
        elif len(b[i:n+i])<n:
            break
        else:
            list2.append(b[i:n+i])

    list3= set(list1).intersection(list2)
    return list3











    # TODO

