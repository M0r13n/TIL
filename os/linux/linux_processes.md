# Processes

## Important commands 

- **ps**	 : report a snapshot of current processes
- **pstree** : display a tree of processes
- **top** 	 : display processes and uptime information
- **nice** 	 : modify scheduling priority
- **renice** : alter priority of running processes
- **kill** 	 : terminate processes
- **uptime** : self explanatory :sunglasses:

## General
Every process has it's own unique **PID**. Processes can be **parents** of other processes. Each process is associated with the permissions of the user who started it.

## Ps
- good starting point is `ps aux` or `ps aux | less`
- customize with `-eo` and pass the desired options to it, e.g. ppid, %cpu, etc.
- --> for a better experience just use **htop**
 



