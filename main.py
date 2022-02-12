import os
import re

workspace = "/mnt/c/Users/kevin/Downloads"
files = "/mnt/c/Users/kevin/Downloads/micelaneus"
pdf = "/mnt/c/Users/kevin/Downloads/pdfs"
imgs = "/mnt/c/Users/kevin/Downloads/images"
pattern_pdf = re.compile(r"[a-z\ ]*(\.pdf)")
pattern_img = re.compile(r"[a-z\ ]*(\.jpg|\.png|\.jpeg)")


def recollect():
    with os.scandir(workspace) as sentinel:
        for e in sentinel:
            move_dir(e) if e.is_file() else print(f"dxr -> {e.name}")


def move_dir(file):
    one = re.search(pattern_pdf, file.name)
    two = re.search(pattern_img, file.name)

    if one:
		# shutil.move(file.path, pdf)
        os.rename(file.path, pdf + '/' + file.name)

    elif two:
        # shutil.move(file.path, imgs)
        os.rename(file.path, imgs + '/' + file.name)

    else:
        print(one)
    # 	shutil.move(file.path , files)


def main():
    recollect()


if __name__ == '__main__':
    main()
