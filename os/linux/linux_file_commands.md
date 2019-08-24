# Working with files

## ls
- list files and directories
- `ls -a`		: list **all** files (also hidden . files)
- `ls -d */`	: list all directories in the current dir
- `ls -i`		: list file's inode index number
- `ls -l`		: also `ll`, list in long format + permissions
- `ls -R`		: list directory tree, (**Pro-Tip**: run in home dir :sunglasses:)
- `ls -sS`		: list file size sorted by file size
- `ls -t`		: sort by time & date	

## touch
- changes the time stamp of a file
- it basically *touches* the file without changing anything
- mainly used for file creation, when there is no content needed 


## mkdir
- make directory
- **md** on ZSH
- `md dir` 			: create directory dir
- `md -p dir/dir`	: create directory dir/dir
- `md -m permission` : create dir and change permissions


## rm & rmdir
- **rmdir** can only remove **empty** dirs
- **rm** deletes basically everything
- my best friend is definitely `rm -rf`

## grep
- global regular expression print
- `-i` ignores case
