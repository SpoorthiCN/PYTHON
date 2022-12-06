# frequency
l = [1, 2, 8, 5, 8, 7, 8]

d= {}

print('enter the element')
largest = max(l)

for i in l:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
		
print(d[largest])
