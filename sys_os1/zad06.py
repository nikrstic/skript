import os

for dirpath, dirname, filenames in os.walk('..'):
    print(dirpath,dirname,filenames)

print('-'*100)