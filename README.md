# Sorting files script 
It's a script that you can add to your crontab config or Schtask on Windows to move files depending its extension. For each move operation a log and snapshot will be saved

## How to use 💡
Script will works on the directory that their path are set in `WORKSPACE` variable in `functions.py` file. So, after put your path just execute:
```python
python3 (py3 on Windows) main.py
```

and your files will be moved depending its extension to three diferent directories.
### Directories:
The script creates three directories, one for documents, other for images & videos and other for miscellaneous files where can you binary files, jupyter notebooks etc. 

### Crontab:
The purpose of the script is to be used on crontab task manager, there you can config how often the script will be executed as follow:
```bash
* * * * * python3 ~/github/project/path/crontab-files/main.py 
```

## Logs 📃
Logs are useful to know which files was moved and where, this log save original file's path and destiny path join with the date and hour of the operation. 
All logs of day are saved at a same file. This file also have the date when was created.

![](https://i.imgur.com/r2dYfJy.png)

## Snapshots 📷
It makes a "capture" in workspace path to know how left it after movement operation and which files or directories left. Like a "second prove" to know which files was moved.

![](https://i.imgur.com/eYm7HxR.png)

Enjoy :bamboo:
