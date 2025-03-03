import datetime
import os
import re

WORKSPACE = "/mnt/c/Users/kevin/Downloads"  # For example I use /Downloads
FILES = f"{WORKSPACE}/miscellaneous"
DOCS = f"{WORKSPACE}/docs"
IMGS = f"{WORKSPACE}/images"
LOGS_PATH = f"{WORKSPACE}/logs"
SNAPSHOTS = f"{WORKSPACE}/logs/snapshots"
DOC_PATTERN = re.compile(r"[a-z\ ]*(\.pdf|\.txt|\.docx|\.xslx|\.markdown)")
IMG_PATTERN = re.compile(r"[a-z\ ]*(\.jpg|\.png|\.jpeg|\.webp|\.mp4|\.gif|\.svg)")
DOCS_COUNT, IMGS_COUNT, FILES_COUNT = 0, 0, 0
CURRENT_DAY = None


def directories() -> None:
    """
    Creates directories to move all files that will be filtered in workspace
    path.
    """
    if not os.path.exists(LOGS_PATH):
        os.mkdir(LOGS_PATH)

    if not os.path.exists(SNAPSHOTS):
        os.mkdir(SNAPSHOTS)

    if not os.path.exists(FILES):
        os.mkdir(FILES)

    if not os.path.exists(DOCS):
        os.mkdir(DOCS)

    if not os.path.exists(IMGS):
        os.mkdir(IMGS)


def filter() -> None:
    """
    Filter between files and directories using const WORKSPACE value as path
    also this const is used as relative path to make others paths to logs
    and snapshots.
    """
    with os.scandir(WORKSPACE) as files:
        for file in files:
            if file.is_file():
                router(file)


def check_last_day_in_log(log_file_path: str) -> str:
    """
    Check the last day separator in the log file to avoid adding duplicates.

    Parameters:
        log_file_path: Path to the log file

    Returns:
        The last recorded day in YYYY-MM-DD format or None if no record found
    """
    if not os.path.exists(log_file_path) or os.path.getsize(log_file_path) == 0:
        return None

    try:
        with open(log_file_path, "r") as f:
            content = f.read()
            # Look for day separators in the format: ------ Monday DD/MM/YYYY -------
            day_separators = re.findall(
                r"------ \w+ (\d{2}/\d{2}/\d{4}) -------", content
            )
            #  DD/MM/YYYY to YYYY-MM-DD
            if day_separators:
                last_day = day_separators[-1]
                day, month, year = last_day.split("/")
                return f"{year}-{month}-{day}"
        return None
    except Exception:
        return None


def log() -> str:
    """
    Return logs_file_path for the current month
    Use it as destiny for each moves operation file creating a directory for logs
    files and also creating these files, each one has the month when was created.
    """
    today = datetime.date.today()
    current_month = today.strftime("%Y-%m")  # Format: YYYY-MM
    logs_file_path: str = f"{LOGS_PATH}/log-{current_month}.txt"

    if not os.path.exists(logs_file_path):
        os.system(f"cd {LOGS_PATH} && touch log-{current_month}.txt")

    # new day separator
    global CURRENT_DAY
    if CURRENT_DAY is None:
        CURRENT_DAY = check_last_day_in_log(logs_file_path)

    today_str = today.strftime("%Y-%m-%d")
    if CURRENT_DAY != today_str:
        CURRENT_DAY = today_str
        add_day_separator(logs_file_path, today)

    return logs_file_path


def add_day_separator(log_file_path: str, date: datetime.date) -> None:
    """
    Add a separator for a new day in the monthly log file.

    Parameters:
        log_file_path: Path to the monthly log file.
        date: The date to add as separator.
    """
    separator = f"\n------ {date.strftime('%A %d/%m/%Y')} -------\n"
    with open(log_file_path, "a") as f:
        f.write(separator)


def rename_log(file_source: str, file_name: str, logs: str, file_destiny: str) -> None:
    """
    Using os.rename to move files renaming them and then make a log to have a register
    for the files moved and where was moved also adding date and hours when this was.

    Parameters:
        file_source: file's origin path.
        file_name: file's name.
        logs: log's file name.
        file_destiny: path where the file would be moved.
    """
    os.rename(file_source, file_destiny + "/" + file_name)

    log_message = f"{file_source} -> {file_destiny} -- {datetime.datetime.now().strftime('%H:%M')}"
    with open(logs, "a") as log_file:
        log_file.write(log_message + "\n")


def router(file) -> None:
    """
    Filter where each file goes using RegExp patterns to know their extension.

    Parameters:
        file: Output from <scandir> function.
    """
    directories()
    log_path: str = log()
    global FILES_COUNT, DOCS_COUNT, IMGS_COUNT

    if re.search(DOC_PATTERN, file.name):
        DOCS_COUNT += 1
        rename_log(file.path, file.name, log_path, DOCS)

    elif re.search(IMG_PATTERN, file.name):
        IMGS_COUNT += 1
        rename_log(file.path, file.name, log_path, IMGS)

    else:
        FILES_COUNT += 1
        rename_log(file.path, file.name, log_path, FILES)


def snapshot() -> None:
    """
    List directories in workspace after the files was moved regarding they extension.
    Then, we can see the state of workspace after to be filtered and cleanned.
    """
    listed_dirs: list[str] = os.listdir(f"{WORKSPACE}")
    date: str = datetime.datetime.now().strftime("%a %d/%m/%y %H:%M")

    current_month = datetime.date.today().strftime("%Y-%m")
    snapshot_path = f"{SNAPSHOTS}/snapshot-{current_month}"

    if not os.path.exists(snapshot_path):
        today_str = datetime.date.today().strftime("%A %d/%m/%Y")
        os.system(f"echo '\n------ {today_str} -------\n' > {snapshot_path}")

    os.system(f"echo {listed_dirs} {date} >> {snapshot_path}")


def count() -> None:
    "Count the number of files moved to each directory"
    global FILES_COUNT, DOCS_COUNT, IMGS_COUNT
    print(
        "-------------------\n",
        f"Files: [{FILES_COUNT}]",
        f"Docs: [{DOCS_COUNT}]",
        f"Images: [{IMGS_COUNT}]",
        f"Check detailed logs at {LOGS_PATH}",
        "-------------------\n",
        sep="\n",
    )
