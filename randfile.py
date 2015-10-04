import os
from random import randint
b=randint(0,100)
home = os.path.expanduser('~')
filename="butts"
ifdone=False
print(home)
for path, subdirs, files in os.walk(home):
    for name in files:
        from random import randint
        a=randint(0,100)
        if a==b:
            #filename=os.path.join(path, name)
            filename=name
            ifdone=True
            break
    if ifdone:
        break

print(filename)
        
