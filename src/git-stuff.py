# pip install gitpython
from git import Repo
import os

# Init repo object from current project dir (which has .git dir)
repo = Repo(os.getcwd())
assert not repo.bare

master_local = repo.commit("master")
master_remote = repo.commit("origin/master")

print(
    f"{str(master_remote)[0:8]}..{str(master_local)[0:8]}")

# Take diff between origin/master and master
diffs = master_remote.diff(master_local)

# List all the files in the diff
for diff in diffs:
    # path can safely use diff.a_path until the change_type is Rename (R)
    path = diff.a_path if diff.change_type != "R" else f"{diff.a_path} => {diff.b_path}"
    print(f"{diff.change_type} {path}")
