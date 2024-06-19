# Script to move files
It's a `Bash` script that you can add to your crontab config or `Schtask` (Windows) or `Crontab` (Linux) to move files depending its extension. For each move operation a log will be saved

## How to use 💡
Script will works on the directory that their path are set in `WORKSPACE` variable in `functions.py` file. So, after put your path just execute:
```python
python3 main.py #py on Windows
```

and your files will be moved depending its extension to three diferent directories. The script will create three directories, one for documents, another for images & videos and one last for miscellaneous files (binary files, jupyter notebooks etc). 

## Logs 📃
Logs are useful to know which files were moved and where, this log saves the original file's path and destiny path join with the date and hour of the operation. 
All logs of the day are saved at a same file. This file also have the date when was created.

![image](https://i.imgur.com/r2dYfJy.png)
|:--:|
| **Output** |

----

:bamboo: ~
