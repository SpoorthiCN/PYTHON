# Birthday
bd={}

for i in range(2):
    print('Enter the key value')
    key=input()

    print('Enter the value')
    value=int(input())
    bd[key]=value
    print (bd)
for i in range(len(bd)):
    print("Enter your friend's name")
    name=input()
    if name in bd:
        print('Birthdate is '+str(bd.get(name)))
else:
    print("Enter your friend's name")
    key1=input()
    print('Enter the birthday date')

    valuel=int(input())
    bd[key1]=valuel
    print (bd)
