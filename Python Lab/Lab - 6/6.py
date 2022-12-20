#replace all occurences of space,comma,dot with :
import re
text = 'Python Exercises, PHP exercises.PAP'
print(re.sub("[ ,.]", ":", text))
