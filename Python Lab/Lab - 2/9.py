#Write a python program to chech entered number is +ve or -ve or 0 and dispay a message (use nested if statement)
num=int(input('Enter a number'))
if num >=0:
    if num==0 :
        print('Number is Zero')
    else:
        print('Number  is positive')
else:
    print('Number is negative')
