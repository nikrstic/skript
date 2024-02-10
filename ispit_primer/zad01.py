import sys

a=' '.join(sys.argv[1:])

print(a)
def recenica(a):
    if (len(a)<=2):
        raise ValueError("prekratak string")
    if not a[0].isupper():
        return False
    if not a[-1] in ["?", ".", "!"]:
        print(a[-1])
        return False
    for i in range(1,len(a)-2):
        if not (a[i].isspace() or a[i].islower()):
            return False
    return True
        
print(recenica(a))
        