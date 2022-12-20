#road as rd
import re
p=re.compile('Road\w*')
r=p.sub('Rd','Road is always a Road')
print(r)
