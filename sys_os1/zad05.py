import sys
import os

if sys.platform == 'win32':
    print(os.system('dir'))
else:
    print(os.system("ls"))

print(os.system("aaaaaaaaa"))
