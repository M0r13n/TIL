#Linux user management

## important files:
- **/etc/passwd**	: user information
- **/etc/shadow**	: encrypted passwords
- **/etc/group** 	: group information
- **/etc/sudoers**	: configuration for sudo

## Add user
- create user with `sudo adduser leon`
- change password with `passwd leon`
- everything will be stored in **/etc/passwd**
- a group witht the same name is added automatically, the so called primary group

## Grant user permissions
- need to change **/etc/sudoers**
- open the file with **visudo** and **NOT** with a regular text editor
- **visudo** ensures 1) only I can change the file and 2) syntax checking
- add an entry: **leon ALL=(ALL) ALL**
- --> username | hosts | which commands as which user

## Switch users
- `su -l leon`
- -l provides a normal environment

## Usermod
- change homedir with `sudo usermod --home /Users/leon leon`
- change the default shell with `sudo usermod --shell /bin/sh leon`
- add a comment with `sudo usermod --comment "A user with a comment" leomn`

## Delete a user
- delete a user with `sudo userdel -r`
- delete all files with **-r** or keep them by omitting


# Groups

Groups are defined as a way to organize users with the same type of access.

## Add group
- `addgroup students`

## Delete group
- `delgroup students`


# Permissions

## important commands
- **chmod**	: change file permissions
- **chown**	: change file owner
- **chgrp**	: change group ownership
- **id**	: print **UID** and **GID**

## Ls
- command is `ls -l [filename]`
- output is similar to : **-rw-r--r--  1 leon  staff  12 12 Aug 16:49 test.txt**
- 1st char		: file type (- means regular file, no directory)
- 2nd-10th char	: permissions for 1) **Owner**, 2) **Group owner**, 3) **Other users**

## Chmod
- commands looks like `chmod u+x test.txt`
- 1st char indicates to whom the new permissions should be applied to
- **+** means adding a permission and **-** means deleting it

## Special bits
- **setuid** : any user can execute that file with owner permission (see **passwd**)
- **setgid** : any user can execute that file with group permission