# ANSI ESC CHARACTERS

Fort a full list see this [link](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors).

- ESC = `\x1b` in hex or `\033` in octal
- Control Sequence Introducer  = CSI = ESC [

### SGR (Select Graphic Rendition)
SGR needs to be wrapped with `CSI m`.

So format is: `CSI CODE m` <-> `\x1b CODE m` (**without whitespaces**).

| Code        | Effect           | Example  |
| ------------- |:-------------:| -----:|
| 0     | RESET | \x1b[0m|
| 5     | Blink | \x1b[5m|
| 7     | Swap Foreground and background color | \x1b[7m|
| 30-37     | Change Foreground color | \x1b[31|
| 40–47     | Change Background color | \x1b[46m|

### Nice examples :-)

```
$ echo "\x1b[46m \x1b[31m \x1b[5m Ultra geile Farben Dingse \x1b[0m"
```
