#Write a python program to print all the values from 1 to 100 skip numbers which are divisible by 4 or 7
i=1
while i <= 100:
   if((i % 4 !=0) and (i % 7 !=0)):
      print(i)
   i=i+1
