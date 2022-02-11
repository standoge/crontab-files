import os
import shutil

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/files"

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
