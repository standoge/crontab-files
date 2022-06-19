# Crontab-task 

It's a script that you can add to your crontab config or Schtask in Windows to filter and move your files, *pdf*, *img*, *others* to different directories. Also for each movement operation it will be saved on a log-file. 

## Directories:
The script creates three directories, one for documents, other for images & videos and other for miscellaneous files. Script will work on the directory that their path are in `WORKSPACE` variable.

## Logs:
Logs are useful to know which files was moved and where, this log save original file's path and destiny path join with the date and hour of the operation. 
All logs of day are saved at a same file. This file also have the date when was created.

![](https://i.imgur.com/r2dYfJy.png)

## Snapshots:
It makes a "capture" in workspace path to know how left it after movement operation and which files or directories left. Like a "second prove" to know which files was moved.

![](https://i.imgur.com/eYm7HxR.png)

Enjoy :bamboo:
