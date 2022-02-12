import os
import shutil
import re

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/files"
pdfs = "/mnt/c/Users/kevin/Downloads/pdfs"
imgs = "/mnt/c/Users/kevin/Downloads/immms"
pattern_pdf = re.compile(r"[a-z\ ]*(\.pdf)")
pattern_img = re.compile(r"[a-z\ ]*(\.jpg|\.png)")

def recollect():
	with os.scandir(workspace) as sentinel:
		for e in sentinel:
			move_dir(e) if e.is_file() else print(f"dxr -> {e.name}") 


def move_dir(file):
	one = re.search(pattern_pdf,file.name)
	two = re.search(pattern_img,file.name)

	if one:
		shutil.move(file.path,pdfs)

	elif two:
		shutil.move(file.path,imgs)

	else:
		print(one)
	# 	shutil.move(file.path , files)

def test(string):
	print("uwu") if re.match(pattern_img, string) else print("todo aml")


def main():
	recollect()


if __name__ == '__main__':
    main()


