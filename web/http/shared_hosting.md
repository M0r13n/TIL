# Shared Web Hosting explained
It's common practice to host multiple domains on a single server with a single IP. This is primarily done to keep costs low and is called [Shared Web Hosting](https://en.wikipedia.org/wiki/Shared_web_hosting_service).

##### How does it work?
Normally the browser queries some DNS server to translate a given domain name into an ip address. 

For example if we lookup [google.com](www.google.com) we get 172.217.168.206 as an ip. Typing this IP into the browser or using curl to get the page's content yields the familiar front page of google.
```sh
$  dig google.com
google.com.		161	IN	A	172.217.168.206
```

Trying the same with [www.example.com](www.example.com) surprisingly fails:
```sh
$  dig example.com                          
example.com.		8285	IN	A	93.184.216.34
```
```sh
$  curl 93.184.216.34                       
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<title>404 - Not Found</title>
	</head>
	<body>
		<h1>404 - Not Found</h1>
	</body>
</html>
```
I this case there are multiple domains hosted on the same server. But why does it work if I type the domain directly into my browser but now when I use the IP. It turns out that browsers send the hostname as part of the request inside the HTTP header. The server uses this hostname to get the requested content. To demonstrate this behaviour we can use curl again and include the hostname as part of the request.

```sh
$  curl 93.184.216.34 -H "Host: example.com"
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    ...
```
