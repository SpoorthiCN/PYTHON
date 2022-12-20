#ph no and email address
import re
p=re.compile('(\(\d{3}\)?[-|.|\s])?\d{3}[-|\.|\s]\d{4}')
r=p.search('my phone number is (412)-765-7676')
print(r.group())

import re
regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid("shreya.gowda@gmail.com")
isValid("spoorthicn11@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")
