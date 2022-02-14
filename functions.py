import os
import re
import datetime

WORKSPACE = "/mnt/c/Users/kevin/Downloads"
FILES = "/mnt/c/Users/kevin/Downloads/miscellaneous"
PDF = "/mnt/c/Users/kevin/Downloads/pdfs"
IMGS = "/mnt/c/Users/kevin/Downloads/images"
LOGS_PATH = f"{WORKSPACE}/logs"
SNAPSHOTS = f"{WORKSPACE}/logs/snapshots"
PDF_PATTERN = re.compile(r"[a-z\ ]*(\.pdf)")
IMG_PATTERN = re.compile(r"[a-z\ ]*(\.jpg|\.png|\.jpeg)")


def recollect():
    with os.scandir(WORKSPACE) as sentinel:
        for e in sentinel:
            move_dir(e) if e.is_file() else print(f"directory -> {e.name}")


def make_log():
    os.mkdir(LOGS_PATH) if not os.path.exists(
        LOGS_PATH) else print("logs_dir already exist")
    log_file_path = f"{LOGS_PATH}/log-{datetime.date.today()}"
    os.system(f"cd {LOGS_PATH} && touch log-{datetime.date.today()}") if not os.path.exists(
        log_file_path) else print("logs file already exist")
    return log_file_path


def move_dir(file):
    log_path = make_log()
    one = re.search(PDF_PATTERN, file.name)
    two = re.search(IMG_PATTERN, file.name)

    if one:
        os.rename(file.path, PDF + '/' + file.name)
        os.system(
            f"echo {file.path} moved to {PDF} >> {log_path} {datetime.datetime.now()}")

    elif two:
        os.rename(file.path, IMGS + '/' + file.name)
        os.system(
            f"echo {file.path} moved to {IMGS} >> {log_path} {datetime.datetime.now()}")

    else:
        os.rename(file.path, FILES + '/' + file.name)
        os.system(
            f"echo {file.path} moved to {FILES} >> {log_path} {datetime.datetime.now()}")


def make_snapshots():
    os.mkdir(SNAPSHOTS) if not os.path.exists(
        SNAPSHOTS) else print("snapshots already exist")
    snapshot = os.listdir(f"{WORKSPACE}")
    os.system(
        f"echo {snapshot} {datetime.datetime.now()}  >> {SNAPSHOTS}/snapshot-{datetime.date.today()}")
