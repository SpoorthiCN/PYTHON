#duplicate elements of the list
def has_dup(v):
    c=0

    for i in range(len(v)):
        for j in range(len(v)-1):
            if v[i]==v[j+1]:
                c=c+1
                print(c)
    if c>1:
        return True
    if c<=1:
        return False
