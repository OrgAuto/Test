import os
from env.properties import *

print(val)
commit_id = get_commit_hash()
delta_changes = get_delta_files(commit_id)

with open(".//Logs//commit.log", "w") as commit_file:
    commit_file.writelines(delta_changes)
    commit_file.close
