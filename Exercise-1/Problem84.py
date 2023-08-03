
# Python Program to Find All File with .txt Extension Present Inside a Directory
import glob,os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)
