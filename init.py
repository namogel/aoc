import os
import shutil

YEAR = "2022"

os.makedirs(YEAR)
os.chdir(YEAR)
for i in range(1, 32):
    folder = f"{i:02d}"
    os.makedirs(folder)
    shutil.copy("../a.py", f"{folder}/a.py")
    with open(f"{folder}/input", "w"):
        pass
