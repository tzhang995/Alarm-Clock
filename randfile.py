import os
home = os.path.expanduser('~')
print(home)
for path, subdirs, files in os.walk(home):
    for name in files:
        print os.path.join(path, name)
