from git import Repo
import os
print(os.getcwd())

repo = Repo(os.getcwd())
assert not repo.bare
print(repo)

print(repo.is_dirty())

print(repo.untracked_files)
