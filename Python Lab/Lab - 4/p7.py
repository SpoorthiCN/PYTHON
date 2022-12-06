# removenum=[]

print('enter the length of a list')

l=int(input())

for i in range(l):
    n=int(input('enter a number'))
    num.append(n)

print('the orignal list is')

print(num)

print('the number to be removed')

n=int(input())

num.remove(n)

print(num)
