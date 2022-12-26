#cumulative sum
def csum(a):
    sum=0
    res=[]
    for i in a:
        sum=sum+i
        res.append(sum)
    print(res)

csum([1,2,3])

