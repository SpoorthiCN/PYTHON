# c)swap two variables using XOR method
x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
x=x^y
y=x^y
x=x^y
print(x,y)
