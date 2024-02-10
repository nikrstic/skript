import os
import shutil
for dirpath, dirnames, filenames in os.walk('.'):
    for file in filenames:
        filepath=os.path.join(dirpath,file)
        ext = os.path.splitext(file)[1]
        #print("Datoteka:", filepath)
        #print("Ekstenzija:", ext)
        trenutni=os.getcwd()
        if ext == ".txt":
            dir_name=os.path.basename(dirpath)
            destination=os.path.join(trenutni,dir_name+'_'+file)
            shutil.copy(filepath,destination)
