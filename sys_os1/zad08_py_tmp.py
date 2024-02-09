import os
import pathlib
import shutil

tmp_dir=pathlib.Path('tmp')
tmp_dir.mkdir(exist_ok=True)
for file in os.listdir():
    curr_file=pathlib.Path(file)
    if os.path.isfile(file) and curr_file.suffix=='.py':
        mod_file=curr_file.with_suffix('.txt')
        shutil.copy(file,tmp_dir.joinpath(mod_file))