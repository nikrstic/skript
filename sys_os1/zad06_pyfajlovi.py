import os

for dirpath, _,filenames in os.walk('..'):
    for file in filenames:
        if not file.endswith('.py'):
            continue
        fullpath=os.path.join(dirpath,file)
        print(fullpath)