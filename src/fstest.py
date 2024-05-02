import fsspec
from pathlib import Path

# gets files from github repo
# its a bit slow

# recursive copy
destination = Path("misc/test_recursive_folder_copy")
destination.mkdir(exist_ok=True, parents=True)
fs = fsspec.filesystem("github", org="genemede", repo="gnmd-mtypes")
lst = fs.ls("data")
print(lst)
#fs.get(fs.ls("data/"), destination.as_posix(), recursive=True)
