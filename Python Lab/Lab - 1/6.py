#Write a python program to solve Quadratic Equation
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
dis=b+b-4*a*c
if dis<0:
    print("Roots are COMPLEX")
elif dis==0:
    print("ONE Root")
else:
    print("Roots are REAL")
