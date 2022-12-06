# hetero
list1 =['amrutha', 3, 8, 'is', 'good girl', 0.3]
print("The original list :" + str(list1))

result_str =[element for element in list1 if isinstance (element, str)]

result_int =[element for element in list1 if isinstance(element, int)]
result_float=[element for element in list1 if isinstance(element, float)]
print("Integer list : " + str(result_int))

print("String list : " + str(result_str))

print("float list : " + str(result_float))
