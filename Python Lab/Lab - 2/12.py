#Write a python program to print sum of natural numbers upto n
n=int(input('Enter a number'))
sum=0
for i in range(1,n):
    sum=sum+i
    print(sum)
    i+=1
