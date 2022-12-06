# uples
tuple=[]

print('enter the length of a list')

l=int(input())

for i in range(l):
    n=int(input('enter a number'))
    tuple.append(n)
print(tuple)
count = tuple.count(1)
print(count)
