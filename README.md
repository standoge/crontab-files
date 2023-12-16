# Script to sort files
It's a `Bash` script that you can add to your crontab config or Schtask on Windows to move files depending its extension. For each move operation a log will be saved

## How to use 💡
Script will works on the directory that their path are set in `WORKSPACE` variable in `functions.py` file. So, after put your path just execute:
```python
python3 (py3 on Windows) main.py
```

and your files will be moved depending its extension to three diferent directories. The script will create three directories, one for documents, another for images & videos and one last for miscellaneous files where can you binary files, jupyter notebooks etc. 

The purpose of the script is to be used on crontab task manager, there you can config how often the script will be executed as follow:
```bash
* * * * * python3 ~/github/project/path/crontab-files/main.py 
```

## Logs 📃
Logs are useful to know which files was moved and where, this log save original file's path and destiny path join with the date and hour of the operation. 
All logs of day are saved at a same file. This file also have the date when was created.

![](https://i.imgur.com/r2dYfJy.png)

----

:bamboo: ~
