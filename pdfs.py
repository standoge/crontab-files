import os
import shutil
import re

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/files"
pattern = re.compile(r"[a-z]*(\.pdf)")

def recollect():
	with os.scandir(workspace) as sentinel:
		for e in sentinel:
			move_dir(e) if e.is_file() else print(f"dxr -> {e.name}") 


def move_dir(file):
	shutil.move(file.path , files)


def main():
	recollect()


if __name__ == '__main__':
    main()