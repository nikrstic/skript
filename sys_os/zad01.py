import sys
import os
a=sys.argv[1]
files_dir=os.listdir()
for x in files_dir:
    print("\t",x,sep='')
    curr1=os.path.join(os.path.pardir)