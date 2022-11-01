# Write a python program to print c)prime numbers from 1 to 100
for n in range(1,101):
    if(n>1):
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)
