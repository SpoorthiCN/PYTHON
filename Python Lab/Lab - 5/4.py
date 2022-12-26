#is_sorted
def is_sorted(list):
    if sorted(list) == list:
        return True
    else:
        return False

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))
