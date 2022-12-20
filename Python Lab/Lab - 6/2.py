#password
import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password =input("Enter the password: ")
result = re.findall(pattern, password)
if (result):
    print ("Valid password")
else:
    print ("Invalid password")
