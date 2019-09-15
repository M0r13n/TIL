
# AHK - Notes
- One cannot merge commands or chain them together, as known from other languages
- The can be multiple hotkeys in **one single file**
- commands can be written with `;`
- as every language it's interpreted Top-To-Bottom

## Structure
A hotkey is defined by `::`, where the **key combo** (trigger) goes on the **left**.
The actual code or content goes **below** those double points and needs to be followed by a `return`. 
A simple hotkey looks like this:

'''ahk
^j::
Send, My First Script
return
'''

## Hotstrings
Hotstrings are used to either expand text (ftw -> For the win) or to launch custom scripts.

### Structure (Hostrings)
A Hotstring has double colons on **both side** (`::btw::`) and the text to replace, goes on the **right**.
Example: `::btw::By The Way`. They can also act as triggers for custom scripts, like:

'''ahk
::btw::
MsgBox, You typed btw.
return
'''

### Key Mappings

| Tables        | Are           |
| ------------- |:-------------:|
| #	   | WIN |
| !	   | ALT |
| ^	   | CTRL |
| +	   | SHIFT |
| &	   | COMBINE |

- '&' requires the previous keys to be hold, before pressing the second key
- '&' only is able to combine **2** triggers, for more I can use things like `If GetKeyState("Shift","p")`

### Send
- has the same special chars as in key mapping
- But it also has a **lot** more, that are defined in curly brackets `{}`
- ** {} ** dont't work as hotkeys
- Curly brackets may be useful, when I actually want to send the exclamation point **!** (`{!}`) and not press **ALT**. 
- examples:
- `Send, {Ctrl down}c{Ctrl up}`
- `Send, ^s`
- `Sleep, 1000      ; Keep the above pressed key down for one second.`
- for long commands use normal brackets `()`
- see also : SendRaw, SendInput, SendPlay, SendEvent

# Variables
- defined with :=
- access value with `%MyVar2%`
