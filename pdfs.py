import os

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/pdfs"
exec_cm = "-exec mv {}"

def recolect():
	with os.scandir(workspace) as sentinel:
		for e in sentinel:
			move_dir(e.name) if e.is_file() else print(f"dxr -> {e.name}") 


def move_dir(name):
	os.system(f"l | grep .pdf | {exec_cm} {files} '\'")



def main():
    recolect()


if __name__ == '__main__':
    main()
