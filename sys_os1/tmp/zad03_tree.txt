import os

def print_tree(curr,n=0):
    files_dirs=os.listdir(curr)
    for x in files_dirs:
        print("\t"*n,x,sep="")
        curr1=os.path.join(curr,x)
        if os.path.isdir(x) and not x.startwith('.'):
            print_tree(curr,n+1)
print_tree(os.path.pardir)