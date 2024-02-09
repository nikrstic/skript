import pathlib

p=pathlib.Path('folder1')

p1=p.joinpath('folder2','folder3')
print(p1)
my_file=p1.joinpath('myfile.txt')
print(my_file)
p1.mkdir(parents=True,exist_ok=True)
p2p=p1.relative_to('folder1')
print(p2p)
with my_file.open("w") as f:
    f.write("hdsjahda")

print(my_file.match('*.txt'),\
      my_file.match('folder3/m*.txt'),
      my_file.match('folder3/*.txt'),
      # ovo nije tacno, posto je folder1 parent folder (sa leve strane)
      my_file.match('folder1/*.txt'),
      )
my_file1=my_file.with_name('myfile1.dat')
p11=p1.with_name('ccc')
print(my_file1,p11)
print(pathlib.Path.cwd())