import os
import re
from datetime import date

WORKSPACE = "/mnt/c/Users/kevin/Downloads"
FILES = "/mnt/c/Users/kevin/Downloads/micelaneus"
PDF = "/mnt/c/Users/kevin/Downloads/pdfs"
IMGS = "/mnt/c/Users/kevin/Downloads/images"
PDF_PATTERN = re.compile(r"[a-z\ ]*(\.pdf)")
IMG_PATTERN = re.compile(r"[a-z\ ]*(\.jpg|\.png|\.jpeg)")


def recollect():
    with os.scandir(WORKSPACE) as sentinel:
        for e in sentinel:
            move_dir(e) if e.is_file() else print(f"directory -> {e.name}")


def make_log():
    LOGS_PATH = f"{WORKSPACE}/logs"
    os.mkdir(LOGS_PATH) if not os.path.exists(LOGS_PATH) else print("dir already exist")
    log_file_path = f"{LOGS_PATH}/log-{date.today()}"
    os.system(f"cd {LOGS_PATH} && touch log-{date.today()}") if not os.path.exists(log_file_path) else print("file already exist")
    # print(log_file_path)
    return log_file_path


def move_dir(file):
    log_path =  make_log()
    one = re.search(PDF_PATTERN, file.name)
    two = re.search(IMG_PATTERN, file.name)

    if one:
		# shutil.move(file.path, pdf)
        os.rename(file.path, PDF + '/' + file.name)
        os.system(f"echo {file.path} to {PDF} >> {log_path}")

    elif two:
        # shutil.move(file.path, imgs)
        os.rename(file.path, IMGS + '/' + file.name)

    else:
        print(one)
    # 	shutil.move(file.path , files)


def main():
    recollect()
    # make_log()


if __name__ == '__main__':
    main()
