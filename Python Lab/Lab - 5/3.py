#middle of the list
def middle(t):
    t.pop(-1)
    t.pop(0)
    return t
t=[1,2,3,4]
print(middle(t))