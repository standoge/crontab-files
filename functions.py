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
    """Filter between files and directories using WORKSPACE const value as path
	   also is this const is used as relative path to make others paths to logs 
	   and snapshots.
	"""

    with os.scandir(WORKSPACE) as sentinel:
        for e in sentinel:
            move_dir(e) if e.is_file() else print(f"dir -> {e.name}")


def log():
	"""Return logs_file_path 
	   Use it as destiny for each move operation file creates directory for logs 
	   files and also create these files, each one has the date when was created.
	"""

	os.mkdir(LOGS_PATH) if not os.path.exists(LOGS_PATH) else print("Directory for logs already exist")
	logs_file_path = f"{LOGS_PATH}/log-{datetime.date.today()}"
	os.system(
		f"cd {LOGS_PATH} && touch log-{datetime.date.today()}") if not os.path.exists(logs_file_path) else print("File for logs already exist")
	return logs_file_path


def rename_print(file_source,file_name,logs, file_destiny):
	"""Using os.rename move files renaming them and then make a log to have a register
	   for the files moved and where was moved also adding date and hours when this was.
	"""

	os.rename(file_source, file_destiny + "/" + file_name)
	os.system(
		f"echo {file_source} move to {file_destiny} >> {logs} {datetime.datetime.now()}")
	


def move_dir(file):
	"""Filter where goes each file using RegExp to know their extension
	"""

	log_path = log()

	if re.search(PDF_PATTERN, file.name):
		rename_print(file.path,file.name,log_path,PDF)

	elif re.search(IMG_PATTERN, file.name):
		rename_print(file.path,file.name,log_path,IMGS)

	else:
		rename_print(file.path,file.name,log_path,FILES)

def snapshot():
	"""List directories in workspace after the files was moved regarding they extension.
	   Then, we can see the state of workspace after to be filtered.
	"""

	os.mkdir(SNAPSHOTS) if not os.path.exists(SNAPSHOTS) else print("Snapshot directory already exist")
	snapshot_dir = os.listdir(f"{WORKSPACE}")
	os.system(
        f"echo {snapshot_dir} {datetime.datetime.now()}  >> {SNAPSHOTS}/snapshot-{datetime.date.today()}")
