# Bind: Address Already in Use

Sometimes I kept hitting this issue, when trying to reopen a socket, right after I closed it. Even if was pretty sure, that I correctly closed the socket. But thankfully I came across this [article](http://hea-www.harvard.edu/~fine/Tech/addrinuse.html) which helped me understand the underlying issue.

# Normal Closure
Both sides need to **FIN** packets and **ACK** each others **FIN** packet to properly close the connection. **FIN** packets are sent by calling either `close()`, `shutdown()` or `exit()`. The **ACK** is sent by the kernel. It is possible that the process finishes before the kernel has released the associated network resource. -> The port is not reusable.

**If both ends send a FIN before either end receives it, both ends will have to go through TIME_WAIT.**

# Solution

### SO_REUSEADDR
By calling `setsockopt` I can set the **SO_REUSEADDR** option, which will allow a process to bind to a port which remains in **TIME_WAIT**. 

```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

### Client closes first
Simply letting the client close the connection avoids **TIME_WAIT**.

# Examples

### Client (remains the same)
```python
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print('Received', repr(data))
```

### Server Broken
```python
import socket
import time

"""
If this program exits it is not possible to use the same port again.

The reason for that is, that the server calls socket.close() and therefor the kernel will hit TIME_WAIT.
"""

HOST = "127.0.01"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        s.close()
        exit(0)
        while True:
            try:
                conn.sendall(b"Hello")
            except BrokenPipeError as e:
                # client closed the connection
                break

```

### Server Working
```python
import socket
import time

"""
This will work repeatedly.

This is because the client closes the connection and then the server closes it. This way
the kernel wont go into TIME_WAIT.
"""

HOST = "127.0.01"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            try:
                conn.sendall(b"Hello")
            except BrokenPipeError as e:
                # client closed the connection
                break
```
