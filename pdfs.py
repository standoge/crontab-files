import os

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/files"

def recolect():
	with os.scandir(workspace) as sentinel:
		for e in sentinel:
			move_dir(e.name) if e.is_file() else print(f"dxr -> {e.name}") 


def move_dir(name):
	os.system(f"mv {name} {files}")


def main():
    recolect()


if __name__ == '__main__':
    main()
