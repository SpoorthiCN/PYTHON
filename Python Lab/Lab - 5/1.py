#nested_sum
def nested_sum(t):
sum=0
for i in t:
    if type(i)==list:
        sum=sum+nested_sum(i)
    else:
        sum=sum+i
    return sum
    a=nested_sum([[1,2],[3],[4,5,6]])
    print(a)

