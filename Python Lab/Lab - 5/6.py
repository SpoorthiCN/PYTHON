#string matching pattern phone no
import re
def isphoneno(s):
    Pattern=re.compile("\d{3}-\d{3}-\d{4")
    return Pattern.match(s)
    s="345-657-7676"
    if(isphoneno(s)):
        print("Valid number")
    else:
            print("Invalid number")
