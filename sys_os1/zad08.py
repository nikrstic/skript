import shutil
import pathlib
import os

pathlib.Path('tmp').mkdir(exist_ok=True)

shutil.copy('01_sys.py','tmp')
shutil.copy('01_sys.py', 'tmp/bbb.py')
shutil.move('tmp/01_sys.py','tmp/aaa.py')
